import sqlite3
from datetime import datetime

DB_NAME = "weather_data.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL,
            humidity INTEGER,
            weather TEXT,
            timestamp TEXT
        )
        """)
        conn.commit()

def save_weather(data):
    if data is None:
        return

    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    timestamp = datetime.utcnow().isoformat()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO weather (city, temperature, humidity, weather, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """, (city, temperature, humidity, weather, timestamp))
        conn.commit()
