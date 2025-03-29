import pandas as pd
import matplotlib.pyplot as plt
import os


def generate_charts_from_excel(excel_path=None):
    EXPORT_DIR = os.path.dirname(excel_path) if excel_path else "exports"
    CHART_DIR = os.path.join(os.path.dirname(__file__), "..", "charts")
    os.makedirs(CHART_DIR, exist_ok=True)

    if not excel_path:
        # Auto-detect the latest Excel file
        all_files = [f for f in os.listdir(EXPORT_DIR) if f.endswith(".xlsx") and "weather_data_combined" in f]
        if not all_files:
            print("❌ No Excel files found in exports directory.")
            return
        excel_path = os.path.join(EXPORT_DIR, sorted(all_files)[-1])
        print(f"🕵️ Auto-detected Excel file: {excel_path}")

    print(f"📂 Received Excel file path: {excel_path}")

    df_forecast = pd.read_excel(excel_path, sheet_name="Forecast")

    try:
        df_pollution = pd.read_excel(excel_path, sheet_name="Pollution")
    except:
        df_pollution = pd.DataFrame()

    df_forecast["datetime"] = pd.to_datetime(df_forecast["datetime"])
    if not df_pollution.empty:
        df_pollution["datetime"] = pd.to_datetime(df_pollution["datetime"])

    cities = df_forecast["city"].dropna().unique()

    for city in cities:
        print(f"🔄 Generating chart for: {city}")
        city_forecast = df_forecast[df_forecast["city"] == city]
        city_pollution = df_pollution[df_pollution["city"] == city] if not df_pollution.empty else pd.DataFrame()

        fig, axes = plt.subplots(3, 1, figsize=(12, 14))
        fig.suptitle(f"Weather Visualizations for {city}", fontsize=16, fontweight="bold")

        # Plot 1: Temperature & Humidity
        axes[0].plot(city_forecast["datetime"], city_forecast["temp"], label="Temperature (°C)", color="red")
        axes[0].plot(city_forecast["datetime"], city_forecast["humidity"], label="Humidity (%)", color="blue")
        axes[0].set_title("Temperature & Humidity Forecast")
        axes[0].legend()
        axes[0].grid(True)

        # Plot 2: Rain + Snow
        axes[1].bar(city_forecast["datetime"], city_forecast["rain_3h"], label="Rain (mm)", color="skyblue")
        axes[1].bar(city_forecast["datetime"], city_forecast["snow_3h"], label="Snow (mm)", color="lightgray",
                    bottom=city_forecast["rain_3h"])
        axes[1].set_title("Rain + Snow Forecast")
        axes[1].legend()
        axes[1].grid(True)

        # Plot 3: Pollution
        if not city_pollution.empty:
            aqi = city_pollution["aqi"].values[0]
            pm25 = city_pollution["pm2_5"].values[0]
            axes[2].bar(["AQI", "PM2.5"], [aqi, pm25], color=["orange", "gray"])
            axes[2].set_title("Air Pollution: AQI & PM2.5")
        else:
            axes[2].text(0.1, 0.5, "No pollution data available", fontsize=12)
        axes[2].grid(True)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        chart_file = os.path.join(CHART_DIR, f"{city.lower().replace(' ', '_')}_weather_chart.png")
        plt.savefig(chart_file)
        plt.close()
        print(f"✅ Chart saved: {chart_file}")
