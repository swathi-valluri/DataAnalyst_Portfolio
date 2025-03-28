import requests
from src.config import API_KEY, DEFAULT_CITY

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_forecast(city=DEFAULT_CITY):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        city_info = data.get("city", {})
        forecasts = data.get("list", [])

        forecast_data = []

        for entry in forecasts:
            weather = entry["weather"][0] if entry["weather"] else {}

            forecast_data.append({
                "city": city_info.get("name"),
                "country": city_info.get("country"),
                "latitude": city_info.get("coord", {}).get("lat"),
                "longitude": city_info.get("coord", {}).get("lon"),
                "timestamp": entry.get("dt"),

                # Weather main
                "weather_main": weather.get("main"),
                "weather_desc": weather.get("description"),
                "weather_icon": weather.get("icon"),

                # Temperature and pressure
                "temp": entry["main"].get("temp"),
                "feels_like": entry["main"].get("feels_like"),
                "temp_min": entry["main"].get("temp_min"),
                "temp_max": entry["main"].get("temp_max"),
                "pressure": entry["main"].get("pressure"),
                "humidity": entry["main"].get("humidity"),

                # Wind
                "wind_speed": entry.get("wind", {}).get("speed"),
                "wind_deg": entry.get("wind", {}).get("deg"),
                "wind_gust": entry.get("wind", {}).get("gust"),

                # Clouds
                "cloudiness": entry.get("clouds", {}).get("all"),

                # Rain/Snow (optional)
                "rain_1h": entry.get("rain", {}).get("1h"),
                "rain_3h": entry.get("rain", {}).get("3h"),
                "snow_1h": entry.get("snow", {}).get("1h"),
                "snow_3h": entry.get("snow", {}).get("3h")
            })

        return forecast_data

    except requests.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return []
