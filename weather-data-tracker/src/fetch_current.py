import requests
from src.config import API_KEY
from src.geocode import get_coordinates

def fetch_current_weather(city):
    coords = get_coordinates(city)
    if not coords:
        print(f"⚠️ Could not resolve location for '{city}'")
        return None

    lat, lon = coords
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        return {
            "city": city,
            "latitude": lat,
            "longitude": lon,
            "timestamp": data.get("dt"),
            "temp": data["main"].get("temp"),
            "feels_like": data["main"].get("feels_like"),
            "humidity": data["main"].get("humidity"),
            "pressure": data["main"].get("pressure"),
            "weather_main": data["weather"][0].get("main") if data["weather"] else None,
            "weather_desc": data["weather"][0].get("description") if data["weather"] else None,
            "wind_speed": data["wind"].get("speed"),
            "wind_deg": data["wind"].get("deg"),
            "cloudiness": data["clouds"].get("all"),
            "country": data["sys"].get("country"),
            "sunrise": data["sys"].get("sunrise"),
            "sunset": data["sys"].get("sunset")
        }

    except requests.RequestException as e:
        print(f"❌ Error fetching current weather for {city}: {e}")
        return None
