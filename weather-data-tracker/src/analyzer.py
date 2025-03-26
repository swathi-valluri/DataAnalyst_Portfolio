import sqlite3

DB_NAME = "weather_data.db"

def average_temperature_by_city():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT city, ROUND(AVG(temperature), 2) AS avg_temp
        FROM weather
        GROUP BY city
        ORDER BY avg_temp DESC
        """)
        return cursor.fetchall()

def city_temp_rank():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        WITH Ranked AS (
            SELECT 
                city,
                temperature,
                timestamp,
                RANK() OVER (PARTITION BY city ORDER BY temperature DESC) AS temp_rank
            FROM weather
        )
        SELECT * FROM Ranked WHERE temp_rank = 1
        """)
        return cursor.fetchall()

def compare_current_to_previous():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        WITH RankedTemps AS (
            SELECT 
                city,
                temperature,
                timestamp,
                LAG(temperature, 1) OVER (PARTITION BY city ORDER BY timestamp) AS prev_temp
            FROM weather
        )
        SELECT 
            city,
            timestamp,
            temperature,
            prev_temp,
            ROUND(temperature - prev_temp, 2) AS temp_diff
        FROM RankedTemps
        WHERE prev_temp IS NOT NULL
        ORDER BY timestamp DESC
        """)
        return cursor.fetchall()
