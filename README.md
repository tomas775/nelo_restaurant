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
- `DELETE /restaurants/{restaurant_id}/`: Delete a restaurant

### Tables
- `GET /tables/`: Get all tables
- `POST /tables/`: Add a new table
- `PUT /tables/{table_id}/`: Update a table
- `DELETE /tables/{table_id}/`: Delete a table

### Reservations
- `POST /reservations/`: Create a new reservation
- `GET /reservations/`: List all reservations
- `DELETE /reservations/{reservation_id}/`: Cancel a reservation

### Search
- `POST /restaurants/search/`: Search for restaurants with available tables


## Usage

Refer to the API documentation at `/docs` after running the application for detailed usage instructions and request/response schemas.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

