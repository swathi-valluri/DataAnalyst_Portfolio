import sqlite3
import pandas as pd

DB_NAME = "weather_data.db"

def clean_weather_data():
    with sqlite3.connect(DB_NAME) as conn:
        df = pd.read_sql_query("SELECT * FROM weather", conn)

    if df.empty:
        print("⚠️ No data available to clean.")
        return

    original_count = len(df)

    # Remove exact duplicates
    df.drop_duplicates(subset=["city", "timestamp"], keep='last', inplace=True)

    # Handle missing temperature/humidity (drop those rows)
    df.dropna(subset=["temperature", "humidity"], inplace=True)

    # Standardize city name formatting
    df["city"] = df["city"].str.strip().str.title()

    cleaned_count = len(df)

    # Save cleaned data to a new table
    with sqlite3.connect(DB_NAME) as conn:
        df.to_sql("weather_cleaned", conn, if_exists="replace", index=False)

    print(f"✅ Cleaned data saved to table 'weather_cleaned'. {original_count - cleaned_count} rows removed.")
