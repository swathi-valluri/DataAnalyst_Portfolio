# src/cleaner.py

import sqlite3
import pandas as pd
from src.config import DB_NAME

def clean_weather_data():
    with sqlite3.connect(DB_NAME) as conn:
        df = pd.read_sql_query("SELECT * FROM weather", conn)

        # Parse timestamps safely to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

        # Drop rows where timestamp couldn't be parsed
        df.dropna(subset=['timestamp'], inplace=True)

        # Remove duplicates: same city & timestamp (not raw string)
        df.drop_duplicates(subset=['city', 'timestamp'], inplace=True)

        df.to_sql("weather_cleaned", conn, if_exists="replace", index=False)

        print(f"✅ Cleaned data saved to table 'weather_cleaned'. {len(df)} rows written.")
