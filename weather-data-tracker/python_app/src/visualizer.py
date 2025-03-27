import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from datetime import datetime, timedelta

DB_NAME = "weather_data.db"
CHART_DIR = "charts"

# Ensure charts directory exists
os.makedirs(CHART_DIR, exist_ok=True)

def plot_temperature_trend(city):
    with sqlite3.connect(DB_NAME) as conn:
        df = pd.read_sql_query("""
            SELECT timestamp, temperature
            FROM weather_cleaned
            WHERE city = ?
            ORDER BY timestamp
        """, conn, params=(city.title(),))

    if df.empty:
        print("⚠️ No data found for that city.")
        return

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['temperature'], marker='o')
    plt.title(f"Temperature Trend - {city.title()}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)

    # Set tight time range around data
    min_time = df['timestamp'].min() - timedelta(hours=12)
    max_time = df['timestamp'].max() + timedelta(hours=12)
    plt.xlim(min_time, max_time)

    # Format X-axis dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d\n%H:%M'))
    plt.gcf().autofmt_xdate()

    plt.tight_layout()

    filename = os.path.join(CHART_DIR, f"temp_trend_{city.lower()}_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.png")
    plt.savefig(filename)
    print(f"✅ Temperature trend saved to {filename}")


def plot_avg_temp_by_city():
    with sqlite3.connect(DB_NAME) as conn:
        df = pd.read_sql_query("""
            SELECT city, AVG(temperature) as avg_temp
            FROM weather_cleaned
            GROUP BY city
            ORDER BY avg_temp DESC
        """, conn)

    if df.empty:
        print("⚠️ No data to visualize.")
        return

    plt.figure(figsize=(10, 5))
    plt.bar(df['city'], df['avg_temp'], color='skyblue')
    plt.title("Average Temperature by City")
    plt.xlabel("City")
    plt.ylabel("Avg Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    filename = os.path.join(CHART_DIR, f"avg_temp_by_city_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.png")
    plt.savefig(filename)
    print(f"✅ Average temperature chart saved to {filename}")
