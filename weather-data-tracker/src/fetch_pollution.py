import requests
from src.config import API_KEY
from src.geocode import get_coordinates

def fetch_air_pollution(city):
    coords = get_coordinates(city)
    if not coords:
        print(f"⚠️ Could not resolve location for '{city}'")
        return None

    lat, lon = coords
    url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("list"):
            entry = data["list"][0]
            return {
                "city": city,
                "latitude": lat,
                "longitude": lon,
                "timestamp": entry["dt"],
                "aqi": entry["main"]["aqi"],
                "co": entry["components"].get("co"),
                "no": entry["components"].get("no"),
                "no2": entry["components"].get("no2"),
                "o3": entry["components"].get("o3"),
                "so2": entry["components"].get("so2"),
                "pm2_5": entry["components"].get("pm2_5"),
                "pm10": entry["components"].get("pm10"),
                "nh3": entry["components"].get("nh3"),
            }
        return None

    except requests.RequestException as e:
        print(f"❌ Error fetching air pollution data for {city}: {e}")
        return None
