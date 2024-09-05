# startup.py
from .database import engine
from .seeder import seed_data
from .models import Base
from sqlalchemy.orm import Session

# Step 1: Drop all existing tables
print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)

# Step 2: Create all tables again
print("Creating tables...")
Base.metadata.create_all(bind=engine)

# Step 3: Seed data into the database
print("Seeding data...")
with Session(engine) as db:
    seed_data(db)

print("Database setup complete!")
