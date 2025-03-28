from src.fetcher import fetch_weather
from src.database import save_weather_data
from src.reporter import export_weather_to_excel

def main():
    city = input("Enter city name (leave blank for default): ").strip() or None
    weather = fetch_weather(city)

    if weather:
        print(f"\n✅ Weather in {weather['city']}:")
        print(f"📅 Timestamp: {weather['dt']}")
        print(f"🌡️ Temperature: {weather['temp']} °C")
        print(f"🥵 Feels Like: {weather['feels_like']} °C")
        print(f"🌬️ Pressure: {weather['pressure']} hPa")
        print(f"💧 Humidity: {weather['humidity']}%")

        # Save to DB
        save_weather_data(weather)
        print("💾 Weather data saved to database.")

        # Ask to export
        export_choice = input("\n📤 Do you want to export all data to Excel? (y/n): ").strip().lower()
        if export_choice == "y":
            export_weather_to_excel()

    else:
        print("⚠️ Failed to fetch weather data.")

if __name__ == "__main__":
    main()
