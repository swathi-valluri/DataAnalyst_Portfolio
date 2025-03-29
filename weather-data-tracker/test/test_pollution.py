import argparse
from src.fetch_pollution import fetch_air_pollution
from src.reporter import export_air_pollution

def main():
    parser = argparse.ArgumentParser(description="Fetch air pollution data for multiple cities.")
    parser.add_argument("cities", nargs="+", help="List of city names (use quotes for multi-word cities)")
    args = parser.parse_args()

    results = []

    for city in args.cities:
        print(f"🌍 Fetching air pollution data for: {city}")
        data = fetch_air_pollution(city)
        if data:
            results.append(data)
        else:
            print(f"⚠️ No pollution data returned for {city}")

    if results:
        export_air_pollution(results)
    else:
        print("❌ No data fetched. Nothing to export.")

if __name__ == "__main__":
    main()
