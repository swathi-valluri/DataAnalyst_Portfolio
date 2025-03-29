import requests
from src.config import API_KEY

def get_coordinates(city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
        return None
    except requests.RequestException as e:
        print(f"❌ Geocoding failed for {city}: {e}")
        return None
