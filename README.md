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

### Restaurants
- `GET /restaurants/`: List all restaurants
- `POST /restaurants/`: Create a new restaurant
- `GET /restaurants/{restaurant_id}/`: Get details of a specific restaurant
- `PUT /restaurants/{restaurant_id}/`: Update a restaurant
- `DELETE /restaurants/{restaurant_id}/`: Delete a restaurant

### Tables
- `GET /restaurants/{restaurant_id}/tables/`: Get tables for a specific restaurant
- `POST /restaurants/{restaurant_id}/tables/`: Add a new table to a restaurant
- `PUT /restaurants/{restaurant_id}/tables/{table_id}/`: Update a table
- `DELETE /restaurants/{restaurant_id}/tables/{table_id}/`: Delete a table

### Reservations
- `POST /restaurants/{restaurant_id}/reservations/`: Create a new reservation
- `GET /restaurants/{restaurant_id}/reservations/`: List all reservations for a restaurant
- `GET /restaurants/{restaurant_id}/reservations/{reservation_id}/`: Get details of a specific reservation
- `PUT /restaurants/{restaurant_id}/reservations/{reservation_id}/`: Update a reservation
- `DELETE /restaurants/{restaurant_id}/reservations/{reservation_id}/`: Cancel a reservation

### Search
- `POST /restaurants/search/`: Search for restaurants with available tables


## Usage

Refer to the API documentation at `/docs` after running the application for detailed usage instructions and request/response schemas.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

