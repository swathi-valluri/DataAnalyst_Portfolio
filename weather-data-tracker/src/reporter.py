import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "weather_data.db"

def export_weather_to_excel():
    with sqlite3.connect(DB_NAME) as conn:
        df = pd.read_sql_query("SELECT * FROM weather", conn)

    if df.empty:
        print("⚠️ No data available to export.")
        return

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.sort_values(by=["city", "timestamp"], inplace=True)

    filename = f"reports/weather_report_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(filename, index=False)

    print(f"✅ Excel report generated: {filename}")
