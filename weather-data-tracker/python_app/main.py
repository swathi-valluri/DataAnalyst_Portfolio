from src.fetcher import fetch_weather_forecast
from src.database import save_weather
from src.cleaner import clean_weather_data
from src.analyzer import average_temperature_by_city, city_temp_rank, compare_current_to_previous
from src.reporter import export_weather_to_excel
from src.visualizer import plot_temperature_trend, plot_avg_temp_by_city


def print_analysis():
    print("\n📊 Average Temperature by City:")
    for row in average_temperature_by_city():
        print(f"{row[0]}: {row[1]}°C")

    print("\n🔥 Hottest Recorded Temp per City:")
    for row in city_temp_rank():
        print(f"{row[0]} | {row[1]}°C @ {row[2]}")

    print("\n📈 Current vs Previous Temperature Change:")
    for row in compare_current_to_previous():
        print(f"{row[0]} | {row[1]} | Now: {row[2]}°C | Prev: {row[3]}°C | Diff: {row[4]}°C")


if __name__ == "__main__":
    print("📦 Weather Data Tracker")
    print("------------------------")

    action = input("Choose: [1] Fetch & Save Weather  [2] Analyze Stored Data  [3] Export Excel Report  [4] Clean Data  [5] Visualize Data: ").strip()

    if action == "1":
        city = input("Enter city name (default = London): ").strip() or "London"
        forecasts = fetch_weather_forecast(city)
        if forecasts:
            save_weather(forecasts)
            print(f"✅ Fetched and saved {len(forecasts)} forecast records for {city}")
        else:
            print("⚠️ No forecast data saved.")

    elif action == "2":
        print_analysis()

    elif action == "3":
        export_weather_to_excel()

    elif action == "4":
        clean_weather_data()

    elif action == "5":
        sub = input("Visualize: [1] Trend by City  [2] Avg Temp by City: ").strip()
        if sub == "1":
            city = input("Enter city name: ").strip()
            plot_temperature_trend(city)
        elif sub == "2":
            plot_avg_temp_by_city()
