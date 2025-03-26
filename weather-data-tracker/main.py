from src.fetcher import fetch_weather

if __name__ == "__main__":
    city = input("Enter city name (leave blank for default): ").strip() or None
    weather_data = fetch_weather(city)

    if weather_data:
        print(f"\n✅ Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']} °C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description'].title()}")
