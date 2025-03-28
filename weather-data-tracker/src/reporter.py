import sqlite3
import pandas as pd
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "weather_data.db")
EXPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "exports")
os.makedirs(EXPORT_DIR, exist_ok=True)

def export_weather_to_excel():
    """Export all weather data from DB to an Excel file."""
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM weather_data ORDER BY dt DESC", conn)
        conn.close()

        if df.empty:
            print("⚠️ No data available in database to export.")
            return

        filename = f"weather_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        filepath = os.path.join(EXPORT_DIR, filename)
        df.to_excel(filepath, index=False)

        print(f"✅ Excel report saved: {filepath}")

    except Exception as e:
        print(f"Error exporting to Excel: {e}")
