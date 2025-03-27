import sqlite3
import pandas as pd
from datetime import datetime

def export_weather_to_excel():
    with sqlite3.connect("weather_data.db") as conn:
        try:
            df = pd.read_sql_query("SELECT * FROM weather_cleaned ORDER BY timestamp", conn)

            # Convert timestamp safely
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            df.dropna(subset=['timestamp'], inplace=True)

            # Export to Excel
            filename = f"reports/weather_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            df.to_excel(filename, index=False)

            print(f"✅ Excel report generated: {filename}")

        except Exception as e:
            print(f"⚠️ Error exporting to Excel: {e}")
