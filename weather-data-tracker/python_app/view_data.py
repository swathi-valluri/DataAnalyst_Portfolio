import sqlite3
import pandas as pd

DB_NAME = "weather_data.db"

def view_table(table_name):
    with sqlite3.connect(DB_NAME) as conn:
        try:
            df = pd.read_sql_query(f"SELECT * FROM {table_name} ORDER BY timestamp DESC", conn)
            if df.empty:
                print(f"⚠️ Table '{table_name}' is empty.")
            else:
                print(f"\n📋 Data from table: {table_name}\n")
                print(df.to_string(index=False))
        except Exception as e:
            print(f"⚠️ Error reading table: {e}")

if __name__ == "__main__":
    print("Available tables: weather, weather_cleaned")
    table = input("Enter table name to view: ").strip()
    view_table(table)
