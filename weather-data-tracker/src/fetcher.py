import requests
from src.config import API_KEY, DEFAULT_CITY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city=DEFAULT_CITY):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # you can change this to 'imperial' if needed
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
