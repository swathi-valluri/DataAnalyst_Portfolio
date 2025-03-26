from src.fetcher import fetch_weather
from src.database import init_db, save_weather

if __name__ == "__main__":
    init_db()
    city = input("Enter city name (leave blank for default): ").strip() or None
    weather_data = fetch_weather(city)

    if weather_data:
        print(f"\n✅ Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']} °C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description'].title()}")

        save_weather(weather_data)
        print("✅ Weather data saved to database.")
