# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

from sqlalchemy import Column, Integer, String, ARRAY

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Store dietary options and endorsements as comma-separated strings
    dietary_options = Column(String, default="")
    endorsements = Column(String, default="")

class Diner(Base):
    __tablename__ = "diners"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Store dietary restrictions as a comma-separated string
    dietary_restrictions = Column(String, default="")


    
class Table(Base):
    __tablename__ = "tables"
    
    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))
    capacity = Column(Integer)
    
    restaurant = relationship("Restaurant", back_populates="tables")

Restaurant.tables = relationship("Table", order_by=Table.id, back_populates="restaurant")

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True, index=True)
    diner_id = Column(Integer, ForeignKey("diners.id"))
    table_id = Column(Integer, ForeignKey("tables.id"))
    time = Column(DateTime)
    
    diner = relationship("Diner")
    table = relationship("Table")
