from src.fetcher import fetch_forecast
from src.database import save_forecast_data
from src.reporter import export_weather_to_excel

def main():
    city_input = input("Enter city name (leave blank for default): ").strip()
    city = city_input if city_input else None

    forecasts = fetch_forecast(city)

    if forecasts:
        print(f"\n✅ Retrieved {len(forecasts)} forecast records for {forecasts[0]['city']}")
        
        # Show a sample (optional)
        sample = forecasts[0]
        print(f"\n📅 Timestamp: {sample['timestamp']}")
        print(f"🌡️ Temperature: {sample['temp']} °C")
        print(f"💧 Humidity: {sample['humidity']}%")
        print(f"🌥️ Weather: {sample['weather_main']} - {sample['weather_desc']}")
        
        # Save all records to DB
        save_forecast_data(forecasts)
        print("💾 Forecast data saved to database.")

        # Ask to export to Excel
        export_choice = input("\n📤 Export data to Excel? (y/n): ").strip().lower()
        if export_choice == "y":
            export_weather_to_excel()

    else:
        print("⚠️ Failed to fetch forecast data.")

if __name__ == "__main__":
    main()
