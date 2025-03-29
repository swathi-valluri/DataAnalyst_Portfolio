import os
import pandas as pd
from datetime import datetime

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "exports")
os.makedirs(EXPORT_DIR, exist_ok=True)

def export_current_weather(data):
    if not data:
        print("⚠️ No current weather data to export.")
        return

    df = pd.DataFrame(data)

    # Convert Unix timestamp to datetime
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")
    df["sunrise"] = pd.to_datetime(df["sunrise"], unit="s")
    df["sunset"] = pd.to_datetime(df["sunset"], unit="s")

    # Generate file name
    filename = f"current_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(EXPORT_DIR, filename)

    df.to_excel(filepath, index=False)
    print(f"✅ Current weather exported to: {filepath}")

def export_forecast_weather(forecasts):
    if not forecasts:
        print("⚠️ No forecast data to export.")
        return

    df = pd.DataFrame(forecasts)

    # Convert timestamp to readable format
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")

    # ✅ Fill missing rain/snow values with 0
    df["rain_3h"] = df["rain_3h"].fillna(0)
    df["snow_3h"] = df["snow_3h"].fillna(0)

    # Save to Excel
    filename = f"forecast_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(EXPORT_DIR, filename)

    df.to_excel(filepath, index=False)
    print(f"✅ Forecast data exported to: {filepath}")

def export_air_pollution(pollution_data):
    if not pollution_data:
        print("⚠️ No air pollution data to export.")
        return

    df = pd.DataFrame(pollution_data)

    # Convert timestamp to readable format
    df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")

    filename = f"pollution_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join(EXPORT_DIR, filename)

    df.to_excel(filepath, index=False)
    print(f"✅ Air pollution data exported to: {filepath}")

