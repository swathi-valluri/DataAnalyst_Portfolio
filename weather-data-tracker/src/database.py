import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "weather_data.db")

def initialize_forecast_table():
    """Creates the forecast_data table if it doesn't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS forecast_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                country TEXT,
                latitude REAL,
                longitude REAL,
                timestamp INTEGER,
                weather_main TEXT,
                weather_desc TEXT,
                weather_icon TEXT,
                temp REAL,
                feels_like REAL,
                temp_min REAL,
                temp_max REAL,
                pressure INTEGER,
                humidity INTEGER,
                wind_speed REAL,
                wind_deg REAL,
                wind_gust REAL,
                cloudiness INTEGER,
                rain_1h REAL,
                rain_3h REAL,
                snow_1h REAL,
                snow_3h REAL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def save_forecast_data(forecast_list):
    """Saves all forecast records (list of dicts) into SQLite DB."""
    if not forecast_list:
        return

    initialize_forecast_table()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        for record in forecast_list:
            cursor.execute("""
                INSERT INTO forecast_data (
                    city, country, latitude, longitude, timestamp,
                    weather_main, weather_desc, weather_icon,
                    temp, feels_like, temp_min, temp_max,
                    pressure, humidity, wind_speed, wind_deg, wind_gust,
                    cloudiness, rain_1h, rain_3h, snow_1h, snow_3h
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                record["city"], record["country"],
                record["latitude"], record["longitude"],
                record["timestamp"],

                record["weather_main"], record["weather_desc"], record["weather_icon"],
                record["temp"], record["feels_like"],
                record["temp_min"], record["temp_max"],
                record["pressure"], record["humidity"],
                record["wind_speed"], record["wind_deg"], record["wind_gust"],
                record["cloudiness"], record["rain_1h"], record["rain_3h"],
                record["snow_1h"], record["snow_3h"]
            ))
        conn.commit()
