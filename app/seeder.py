# seeder.py
from sqlalchemy.orm import Session
from .models import Diner, Restaurant, Table, Reservation
from datetime import datetime, timedelta

def seed_data(db: Session):
    # Step 1: Create Diners
    diners = [
        {"name": "Jack", "dietary_restrictions": "Vegetarian"},
        {"name": "Jill", "dietary_restrictions": "Gluten-Free"},
        {"name": "Jane", "dietary_restrictions": "Vegan"}
    ]

    diner_objects = []
    for diner_data in diners:
        diner = Diner(name=diner_data["name"], dietary_restrictions=diner_data["dietary_restrictions"])
        db.add(diner)
        diner_objects.append(diner)
    db.commit()

    # Step 2: Create Restaurants and Tables
    restaurants_data = [
        {"name": "Lardo", "endorsements": "Vegetarian, Gluten-Free", "tables": [(2, 4), (4, 2), (6, 1)]},
        {"name": "Panadería Rosetta", "endorsements": "Vegetarian, Gluten-Free", "tables": [(2, 3), (4, 2)]},
        {"name": "Tetetlán", "endorsements": "Paleo, Gluten-Free", "tables": [(2, 4), (4, 2), (6, 1)]},
        {"name": "Falling Piano Brewing Co", "endorsements": "", "tables": [(2, 5), (4, 5), (6, 5)]},
        {"name": "u.to.pi.a", "endorsements": "Vegan, Vegetarian", "tables": [(2, 2)]}
    ]

    for restaurant_data in restaurants_data:
        restaurant = Restaurant(name=restaurant_data["name"], endorsements=restaurant_data["endorsements"])
        db.add(restaurant)
        db.commit()  # Commit each restaurant before creating tables

        # Add tables to the restaurant
        for capacity, count in restaurant_data["tables"]:
            for _ in range(count):
                table = Table(restaurant_id=restaurant.id, capacity=capacity)
                db.add(table)
        db.commit()

    print("Seeding complete!")
