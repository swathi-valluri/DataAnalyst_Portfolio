import sqlite3
import os
from datetime import datetime

# Define the path for your SQLite database
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "weather_data.db")

def initialize_db():
    """Create the weather_data table if it doesn't exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                dt INTEGER,
                temp REAL,
                feels_like REAL,
                pressure INTEGER,
                humidity INTEGER,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def save_weather_data(data):
    """Insert a weather record into the database."""
    initialize_db()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO weather_data (city, dt, temp, feels_like, pressure, humidity)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["city"],
            data["dt"],
            data["temp"],
            data["feels_like"],
            data["pressure"],
            data["humidity"]
        ))
        conn.commit()
