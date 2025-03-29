import argparse
from src.fetch_current import fetch_current_weather
from src.fetch_forecast import fetch_forecast
from src.fetch_pollution import fetch_air_pollution
from src.visualizer import generate_charts_from_excel
from datetime import datetime
import pandas as pd
import os

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "exports")
os.makedirs(EXPORT_DIR, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Weather Data Tracker CLI")
    parser.add_argument("--type", choices=["current", "forecast", "pollution", "all"], required=True,
                        help="Type of data to fetch")
    args = parser.parse_args()

    cities_input = input("🌍 Enter city names separated by comma: ")
    cities = [city.strip() for city in cities_input.split(",") if city.strip()]

    if not cities:
        print("⚠️ No valid cities provided.")
        return

    current_data, forecast_data, pollution_data = [], [], []

    if args.type in ["current", "all"]:
        for city in cities:
            print(f"\n🌇 Fetching current weather for: {city}")
            result = fetch_current_weather(city)
            if result:
                current_data.append(result)

    if args.type in ["forecast", "all"]:
        for city in cities:
            print(f"\n📅 Fetching forecast for: {city}")
            forecasts = fetch_forecast(city)
            if forecasts:
                print(f"✅ {len(forecasts)} entries fetched for {city}")
                forecast_data.extend(forecasts)

    if args.type in ["pollution", "all"]:
        for city in cities:
            print(f"\n💨 Fetching air pollution for: {city}")
            pollution = fetch_air_pollution(city)
            if pollution:
                pollution_data.append(pollution)

    # 🔄 Export everything into a single Excel file with sheets
    filename = f"weather_data_combined_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(EXPORT_DIR, filename)

    with pd.ExcelWriter(filepath) as writer:
        if current_data:
            pd.DataFrame(current_data).to_excel(writer, sheet_name="Current", index=False)
        if forecast_data:
            df_forecast = pd.DataFrame(forecast_data)
            df_forecast["datetime"] = pd.to_datetime(df_forecast["timestamp"], unit="s")
            df_forecast["rain_3h"] = df_forecast["rain_3h"].fillna(0)
            df_forecast["snow_3h"] = df_forecast["snow_3h"].fillna(0)
            df_forecast.to_excel(writer, sheet_name="Forecast", index=False)
        if pollution_data:
            df_pollution = pd.DataFrame(pollution_data)
            df_pollution["datetime"] = pd.to_datetime(df_pollution["timestamp"], unit="s")
            df_pollution.to_excel(writer, sheet_name="Pollution", index=False)

    print(f"\n📄 Combined weather data exported to: {filepath}")

    # 📊 Send to visualizer
    print(f"\n🎯 Sending to visualizer: {filepath}")
    generate_charts_from_excel(filepath)


if __name__ == "__main__":
    main()
