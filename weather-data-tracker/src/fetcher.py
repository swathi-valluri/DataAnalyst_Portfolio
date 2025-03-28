import requests
from src.config import API_KEY, DEFAULT_CITY
from src.geo import get_coordinates

ONE_CALL_URL = "https://api.openweathermap.org/data/3.0/onecall"

def fetch_weather(city=DEFAULT_CITY):
    coords = get_coordinates(city)
    if not coords:
        return None

    lat, lon = coords
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",  # Change to 'imperial' if needed
        "exclude": "minutely,hourly,daily,alerts"
    }

    try:
        response = requests.get(ONE_CALL_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract selected fields for analysis
        current = data.get("current", {})
        return {
            "city": city,
            "dt": current.get("dt"),
            "temp": current.get("temp"),
            "feels_like": current.get("feels_like"),
            "pressure": current.get("pressure"),
            "humidity": current.get("humidity")
        }

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
