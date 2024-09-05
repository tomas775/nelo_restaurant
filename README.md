# Restaurant Reservation API

This FastAPI-based application provides endpoints for managing restaurant reservations and table availability.

## Features

- Search for restaurants with available tables
- List all restaurants
- Create new restaurants
- View tables for a specific restaurant

## Setup

1. Install dependencies:
   ```
   pip install fastapi sqlalchemy
   ```

2. Set up your database connection in `database.py`

3. Run the application:
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

## License

[MIT](https://choosealicense.com/licenses/mit/)

```sh {"id":"01J71VESM129HJPK4D2K4AD0NF"}

```