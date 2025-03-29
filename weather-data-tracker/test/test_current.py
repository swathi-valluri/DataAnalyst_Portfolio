import argparse
from src.fetch_current import fetch_current_weather
from src.reporter import export_current_weather

def main():
    parser = argparse.ArgumentParser(description="Fetch current weather for given cities.")
    parser.add_argument("cities", nargs="+", help="City names (use quotes for multi-word cities)")
    args = parser.parse_args()

    results = []

    for city in args.cities:
        print(f"🌍 Fetching current weather for: {city}")
        weather = fetch_current_weather(city)
        if weather:
            results.append(weather)

    if results:
        export_current_weather(results)
    else:
        print("⚠️ No weather data fetched.")

if __name__ == "__main__":
    main()
