import requests
from datetime import datetime
from src.config import API_KEY

def fetch_weather_forecast(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "list" not in data:
            print(f"⚠️ API error for {city}: {data.get('message', 'Unknown error')}")
            return []

        # Extract multiple forecast records
        forecasts = []
        for item in data["list"]:
            forecasts.append({
                "city": data["city"]["name"],
                "temperature": item["main"]["temp"],
                "humidity": item["main"]["humidity"],
                "weather": item["weather"][0]["description"],
                "timestamp": item["dt_txt"]
            })

        return forecasts

    except Exception as e:
        print(f"❌ Failed to fetch weather data: {e}")
        return []
