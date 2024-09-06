from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
from . import models
from . import schemas
import logging
from . import utils

DIETARY_OPTIONS = {"vegan", "paleo", "gluten-free", "halal", "kosher"}

# Main function to get available restaurants based on diners' restrictions and time
def get_available_restaurants(db: Session, diners: list, time: datetime):
    logging.info("Received search request for time: %s", time)

    # Step 1: Extract all dietary restrictions from the diners
    dietary_restrictions = set()
    for diner in diners:
        dietary_restrictions.update(diner.dietary_restrictions)

    logging.info("Collected dietary restrictions: %s", dietary_restrictions)
    group_size = len(diners)
    logging.info("Group size: %d", group_size)

    matching_restaurants = get_matching_restaurants(db, dietary_restrictions)
    if not matching_restaurants:
        logging.info("No restaurants found that meet dietary restrictions.")
        return []

    available_restaurants = get_available_restaurants_with_tables(db, matching_restaurants, group_size, time)
    if not available_restaurants:
        logging.info("No available restaurants with tables.")
        return []

    return available_restaurants

# Function to get restaurants matching all dietary restrictions
def get_matching_restaurants(db: Session, dietary_restrictions: set):
    matching_restaurants = []
    
    for restaurant in db.query(models.Restaurant).all():
        restaurant_dietary_options = set(utils.deserialize_list(restaurant.dietary_options))
        logging.info(f"Checking restaurant: {restaurant.name} with dietary options: {restaurant_dietary_options}")

        if can_accommodate(restaurant_dietary_options, dietary_restrictions):
            matching_restaurants.append(restaurant)
            logging.info(f"Restaurant {restaurant.name} can accommodate the dietary restrictions")
        else:
            logging.info(f"Restaurant {restaurant.name} does NOT accommodate the dietary restrictions")
    
    return matching_restaurants

def can_accommodate(restaurant_dietary_options: set, restrictions: set):
    return restrictions.issubset(restaurant_dietary_options)

# Function to create a restaurant with endorsements and dietary options
def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    # Serialize the list of dietary options and endorsements
    serialized_dietary_options = utils.serialize_list(restaurant.dietary_options)
    serialized_endorsements = utils.serialize_list(restaurant.endorsements)
    
    # Create a new Restaurant instance
    new_restaurant = models.Restaurant(
        name=restaurant.name, 
        dietary_options=serialized_dietary_options,
        endorsements=serialized_endorsements
    )
    
    db.add(new_restaurant)
    try:
        db.commit()
        db.refresh(new_restaurant)
        
        # Deserialize the dietary options and endorsements before returning
        new_restaurant.dietary_options = utils.deserialize_list(new_restaurant.dietary_options)
        new_restaurant.endorsements = utils.deserialize_list(new_restaurant.endorsements)
        
        return new_restaurant
    except IntegrityError:
        db.rollback()
        raise Exception("Restaurant with this name already exists")


# Function to create a diner with dietary restrictions
def create_diner(db: Session, name: str, dietary_restrictions: list):
    serialized_restrictions = utils.serialize_list(dietary_restrictions)
    
    diner = models.Diner(name=name, dietary_restrictions=serialized_restrictions)
    db.add(diner)
    db.commit()
    db.refresh(diner)
    
    diner.dietary_restrictions = utils.deserialize_list(diner.dietary_restrictions)
    
    return diner

# Function to get all diners (deserialize when reading)
def get_all_diners(db: Session):
    diners = db.query(models.Diner).all()
    
    for diner in diners:
        diner.dietary_restrictions = utils.deserialize_list(diner.dietary_restrictions)
    return diners

# Function to get all restaurants (deserialize endorsements and dietary options)
def get_all_restaurants(db: Session):
    restaurants = db.query(models.Restaurant).all()
    
    for restaurant in restaurants:
        restaurant.dietary_options = utils.deserialize_list(restaurant.dietary_options)
        restaurant.endorsements = utils.deserialize_list(restaurant.endorsements)
    
    return restaurants

# Function to check if restaurant tables are available and match the group size
def get_available_restaurants_with_tables(db: Session, restaurants: list, group_size: int, time: datetime):
    available_restaurants = []
    for restaurant in restaurants:
        available_table = find_available_table(db, restaurant, group_size, time)
        if available_table:
            available_restaurants.append({
                "name": restaurant.name,
                "endorsements": utils.deserialize_list(restaurant.endorsements),
                "table_id": available_table.id,
                "capacity": available_table.capacity
            })
    return available_restaurants

# Function to find an available table that meets the group size and has no overlapping reservation
def find_available_table(db: Session, restaurant: models.Restaurant, group_size: int, time: datetime):
    tables = db.query(models.Table).filter(models.Table.restaurant_id == restaurant.id).all()
    for table in tables:
        logging.info("Checking table with capacity %d at restaurant %s", table.capacity, restaurant.name)
        if table.capacity >= group_size and is_table_available(db, table, time):
            logging.info("Table at restaurant %s is available", restaurant.name)
            return table
    logging.info("No available table at restaurant %s", restaurant.name)
    return None

# Function to check if a table is available (no overlapping reservation within 2 hours before/after)
def is_table_available(db: Session, table: models.Table, time: datetime):
    two_hours_before = time - timedelta(hours=2)
    two_hours_after = time + timedelta(hours=2)
    
    overlapping_reservations = db.query(models.Reservation).filter(
        models.Reservation.table_id == table.id,
        models.Reservation.time.between(two_hours_before, two_hours_after)
    ).first()
    
    return overlapping_reservations is None

# Function to create a reservation for a diner at a specific table and time
def create_reservation(db: Session, diner_id: int, table_id: int, time: datetime):
    overlapping_reservation = db.query(models.Reservation).filter(
        models.Reservation.diner_id == diner_id,
        models.Reservation.time.between(time, time + timedelta(hours=2))
    ).first()

    if overlapping_reservation:
        raise Exception("Diner has an overlapping reservation.")

    new_reservation = models.Reservation(diner_id=diner_id, table_id=table_id, time=time)
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    
    return new_reservation

# Function to delete a reservation by its ID
def delete_reservation(db: Session, reservation_id: int):
    db.query(models.Reservation).filter(models.Reservation.id == reservation_id).delete()
    db.commit()

# Function to get all reservations
def get_all_reservations(db: Session):
    return db.query(models.Reservation).all()

# Function to create a table
def create_table(db: Session, table: schemas.TableBase):
    new_table = models.Table(**table.dict())
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table

# Function to get all tables
def get_all_tables(db: Session):
    return db.query(models.Table).all()

# Function to get tables by restaurant
def get_tables_by_restaurant(db: Session, restaurant_id: int):
    return db.query(models.Table).filter(models.Table.restaurant_id == restaurant_id).all()

# Function to update a table
def update_table(db: Session, table_id: int, table: schemas.TableBase):
    db_table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if db_table is None:
        raise Exception("Table not found")
    
    for key, value in table.dict().items():
        setattr(db_table, key, value)
    
    db.commit()
    db.refresh(db_table)
    return db_table

# Function to delete a table
def delete_table(db: Session, table_id: int):
    db_table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if db_table is None:
        raise Exception("Table not found")
    
    db.delete(db_table)
    db.commit()
