import requests
from src.config import API_KEY

GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_coordinates(city_name, limit=1):
    params = {
        "q": city_name,
        "limit": limit,
        "appid": API_KEY
    }

    try:
        response = requests.get(GEOCODE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            print(f"❌ No coordinates found for '{city_name}'")
            return None

        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon

    except requests.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None
