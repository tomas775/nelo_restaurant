# schemas.py
from pydantic import BaseModel
from typing import List
from datetime import datetime


    
class DinerBase(BaseModel):
    name: str
    dietary_restrictions: List[str]  # Keep this as a list in the schema

class DinerCreate(DinerBase):
    pass

class Diner(DinerBase):
    id: int

    class Config:
        from_attributes = True
        
# Restaurant Schemas
class RestaurantBase(BaseModel):
    name: str
    dietary_options: List[str]  # List of supported dietary options from the fixed set
    endorsements: List[str]

class RestaurantCreate(RestaurantBase):
   pass

class RestaurantResponse(RestaurantBase):

    class Config:
        from_attributes = True

class Restaurant(RestaurantBase):
    id: int

    class Config:
        from_attributes = True

# Table Schemas (Optional if needed for more granular responses)
class TableBase(BaseModel):
    restaurant_id: int
    capacity: int

class Table(TableBase):
    id: int

    class Config:
        from_attributes = True

# Reservation Schemas
class ReservationBase(BaseModel):    
    table_id: int
    time: datetime

class ReservationCreate(ReservationBase):
    diner_ids: List[int]
    class Config:
        from_attributes = True

class Reservation(ReservationBase):
    diner_id: int
    id: int

    class Config:
        from_attributes = True

# Search Request Schema
class SearchRequest(BaseModel):
    diners: List[DinerBase]
    time: datetime
