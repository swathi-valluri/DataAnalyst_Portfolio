import os
from dotenv import load_dotenv

DB_NAME = "weather_data.db"

# Load values from .env file into environment
load_dotenv()

# Access config values
API_KEY = os.getenv("OPENWEATHER_API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "London")

