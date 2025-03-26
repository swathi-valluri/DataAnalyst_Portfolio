from src.fetcher import fetch_weather
from src.database import init_db, save_weather
from src.analyzer import average_temperature_by_city, city_temp_rank, compare_current_to_previous

def print_analysis():
    print("\nAverage Temperature by City:")
    for row in average_temperature_by_city():
        print(f"{row[0]}: {row[1]}°C")

    print("\nHottest Recorded Temp per City:")
    for row in city_temp_rank():
        print(f"{row[0]} | {row[1]}°C @ {row[2]}")

    print("\nCurrent vs Previous Temperature Change:")
    for row in compare_current_to_previous():
        print(f"{row[0]} | {row[1]} | Now: {row[2]}°C | Prev: {row[3]}°C | Diff: {row[4]}°C")

if __name__ == "__main__":
    init_db()
    action = input("Choose: [1] Fetch & Save Weather  [2] Analyze Stored Data: ").strip()

    if action == "1":
        city = input("Enter city name (leave blank for default): ").strip() or None
        data = fetch_weather(city)
        if data:
            print(f"\n✅ Weather in {data['name']}: {data['main']['temp']}°C")
            save_weather(data)
            print("✅ Weather data saved to database.")
    elif action == "2":
        print_analysis()
