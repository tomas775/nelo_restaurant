from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from .. import crud, schemas, database
from typing import List
import logging

router = APIRouter()

# Endpoint to search for restaurants with an available table
@router.post("/restaurants/search/", response_model=List[schemas.RestaurantResponse])
def search_restaurant(request: schemas.SearchRequest, db: Session = Depends(database.get_db)):
    # Log incoming data
    logging.info("Request received: %s", request)
    
    diners = request.diners
    reservation_time = request.time

    # Log diner structure
    logging.info("Diners: %s", diners)

    # Call the CRUD function with the diners and time
    restaurants = crud.get_available_restaurants(db, diners, reservation_time)
    
    if not restaurants:
        raise HTTPException(status_code=404, detail="No restaurants available.")
    
    return restaurants

# Endpoint to read all restaurants
@router.get("/restaurants/", response_model=list[schemas.RestaurantResponse])
def read_restaurants(db: Session = Depends(database.get_db)):
    return crud.get_all_restaurants(db)

# Endpoint to create a new restaurant
@router.post("/restaurants/", response_model=schemas.Restaurant)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_restaurant(db, restaurant=restaurant)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to read tables for a specific restaurant
@router.get("/restaurants/{restaurant_id}/tables/", response_model=list[schemas.Table])
def read_restaurant_tables(restaurant_id: int, db: Session = Depends(database.get_db)):
    tables = crud.get_tables_by_restaurant(db, restaurant_id=restaurant_id)
    if not tables:
        raise HTTPException(status_code=404, detail="No tables found for this restaurant")
    return tables