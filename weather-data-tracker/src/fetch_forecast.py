import requests
from src.config import API_KEY
from src.geocode import get_coordinates

def fetch_forecast(city):
    coords = get_coordinates(city)
    if not coords:
        print(f"⚠️ Could not resolve location for '{city}'")
        return []

    lat, lon = coords
    url = "https://api.openweathermap.org/data/2.5/forecast"
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
        city_info = data.get("city", {})
        forecasts = data.get("list", [])

        parsed = []
        for entry in forecasts:
            weather = entry["weather"][0] if entry["weather"] else {}
            parsed.append({
                ""city": city,  
                "country": city_info.get("country"),
                "latitude": lat,
                "longitude": lon,
                "timestamp": entry.get("dt"),
                "datetime_txt": entry.get("dt_txt"),
                "temp": entry["main"].get("temp"),
                "feels_like": entry["main"].get("feels_like"),
                "humidity": entry["main"].get("humidity"),
                "pressure": entry["main"].get("pressure"),
                "weather_main": weather.get("main"),
                "weather_desc": weather.get("description"),
                "wind_speed": entry["wind"].get("speed"),
                "wind_deg": entry["wind"].get("deg"),
                "cloudiness": entry["clouds"].get("all"),
                "rain_3h": entry.get("rain", {}).get("3h"),
                "snow_3h": entry.get("snow", {}).get("3h")
            })

        return parsed

    except requests.RequestException as e:
        print(f"❌ Error fetching forecast for {city}: {e}")
        return []
