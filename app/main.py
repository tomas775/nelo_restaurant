# app/main.py
from fastapi import FastAPI
from .api import reservations
from .api import diners
from .api import restaurants
from .database import engine, Base
from .seeder import seed_data
import logging

app = FastAPI()


# Initialize logging
logging.basicConfig(level=logging.INFO)

Base.metadata.create_all(bind=engine)
# Include API routes
app.include_router(reservations.router)
app.include_router(diners.router)
app.include_router(restaurants.router)
