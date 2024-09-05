# Restaurant Reservation API

This FastAPI-based application provides endpoints for managing restaurant reservations and table availability.

## Features

- Search for restaurants with available tables
- List all restaurants
- Create new restaurants
- View tables for a specific restaurant

## Setup

1. Set up a Python virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```
   pip3 install -r requirements.txt
   ```

3. Set up your database connection in `database.py`

4. Run the startup script to populate initial data:
   ```
   python3 startup.py
   ```

5. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `POST /restaurants/search/`: Search for restaurants with available tables
- `GET /restaurants/`: List all restaurants
- `POST /restaurants/`: Create a new restaurant
- `GET /restaurants/{restaurant_id}/tables/`: Get tables for a specific restaurant

## Usage

Refer to the API documentation at `/docs` after running the application for detailed usage instructions and request/response schemas.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

