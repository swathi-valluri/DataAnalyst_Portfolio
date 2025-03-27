# src/database.py

import sqlite3
from src.config import DB_NAME

def save_weather(forecasts):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                temperature REAL,
                humidity INTEGER,
                weather TEXT,
                timestamp TEXT
            )
        """)

        for entry in forecasts:
            cursor.execute("""
                INSERT INTO weather (city, temperature, humidity, weather, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (entry['city'], entry['temperature'], entry['humidity'], entry['weather'], entry['timestamp']))
