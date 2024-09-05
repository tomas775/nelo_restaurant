# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Diner(Base):
    __tablename__ = "diners"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dietary_restrictions = Column(String)  # Comma-separated values

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    endorsements = Column(String)  # Comma-separated values

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
