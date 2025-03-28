import requests
from src.config import API_KEY, DEFAULT_CITY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city=DEFAULT_CITY):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "city": data.get("name"),
            "dt": data.get("dt"),
            "temp": data["main"].get("temp"),
            "feels_like": data["main"].get("feels_like"),
            "pressure": data["main"].get("pressure"),
            "humidity": data["main"].get("humidity"),
        }

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
