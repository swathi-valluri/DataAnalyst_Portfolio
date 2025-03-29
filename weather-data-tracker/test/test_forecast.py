import argparse
from src.fetch_forecast import fetch_forecast
from src.reporter import export_forecast_weather

def main():
    parser = argparse.ArgumentParser(description="Fetch 5-day / 3-hour forecasts for multiple cities.")
    parser.add_argument("cities", nargs="+", help="List of cities (use quotes for multi-word names)")
    args = parser.parse_args()

    all_forecasts = []

    for city in args.cities:
        print(f"🌍 Fetching 5-day forecast for: {city}")
        forecasts = fetch_forecast(city)
        if forecasts:
            all_forecasts.extend(forecasts)
        else:
            print(f"⚠️ No forecast data for {city}")

    if all_forecasts:
        export_forecast_weather(all_forecasts)
    else:
        print("❌ No data fetched. Nothing to export.")

if __name__ == "__main__":
    main()
