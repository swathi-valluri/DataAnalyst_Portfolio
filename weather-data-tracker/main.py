import argparse
from src.fetcher import fetch_forecast
from src.database import save_forecast_data
from src.reporter import export_weather_to_excel

def main():
    parser = argparse.ArgumentParser(description="Weather Forecast Tracker")
    parser.add_argument("cities", nargs="+", help="List of city names to fetch weather for")
    args = parser.parse_args()

    cities = args.cities
    all_forecasts = []

    for city in cities:
        print(f"\n🌍 Fetching forecast for: {city}")
        forecasts = fetch_forecast(city)

        if forecasts:
            print(f"✅ {len(forecasts)} entries fetched for {city}")
            save_forecast_data(forecasts)
            all_forecasts.extend(forecasts)
        else:
            print(f"⚠️ Failed to fetch data for {city}")

    if all_forecasts:
        print(f"\n💾 Saved forecast data for {len(cities)} cities.")
        export_choice = input("\n📤 Export combined data to Excel? (y/n): ").strip().lower()
        if export_choice == "y":
            export_weather_to_excel()
    else:
        print("⚠️ No data fetched — nothing to export.")

if __name__ == "__main__":
    main()
