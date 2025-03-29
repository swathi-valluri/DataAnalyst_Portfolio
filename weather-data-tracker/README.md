# 🌦 Weather Data Tracker using OpenWeatherMap API

## 📌 Project Overview
The **Weather Data Tracker** is a modular Python project designed to:

- Fetch **current weather**, **5-day forecasts**, and **air pollution** data from the OpenWeatherMap API
- Store and export structured datasets to Excel files
- Support multiple cities dynamically via CLI
- Provide data in formats suitable for Excel/Tableau analysis

All modules are organized under `src/` and can be extended independently.

---

## ✅ Features Implemented

- 🔑 API key loading from `.env`
- 📍 City-to-coordinate geocoding (OpenWeatherMap Geo API)
- 📅 Fetching:
  - **Current Weather** (`/data/2.5/weather`)
  - **5-Day Forecasts** (`/data/2.5/forecast`)
  - **Air Pollution** (`/data/2.5/air_pollution`)
- 📄 Structured Excel export for each type of data
- 🧠 CLI-based city input: `python test_current.py London "New York"`
- 📊 Optional: Fill missing `rain_3h`, `snow_3h` values with `0`

---

## 🏠 Project Structure
```
weather-data-tracker/
├── main.py                     # (Optional CLI runner)
├── .env.sample                 # Sample config with API key
├── pyproject.toml              # Poetry config file
├── exports/                    # All Excel output files
├── weather_data.db             # (Optional) SQLite DB
├── test_current.py             # Test script for current weather
├── test_forecast.py            # Test script for forecast
├── test_pollution.py           # Test script for pollution
├── src/
│   ├── config.py               # Loads environment/API key
│   ├── geocode.py              # Converts city name → lat/lon
│   ├── fetch_current.py        # Fetches current weather
│   ├── fetch_forecast.py       # Fetches 5-day forecast
│   ├── fetch_pollution.py      # Fetches air pollution data
│   ├── reporter.py             # Excel export logic
```

---

## ⚙️ Setup Instructions

### 1. Clone and Install
```bash
git clone https://github.com/your-username/weather-data-tracker.git
cd weather-data-tracker
poetry install
```

### 2. Configure API Key
Create a `.env` file:
```
OPENWEATHER_API_KEY=your_real_api_key
DEFAULT_CITY=London
```

### 3. Run Modules Individually
```bash
# Current weather:
python test_current.py London "New York"

# 5-day forecast:
python test_forecast.py London Tokyo

# Air pollution:
python test_pollution.py Mumbai "San Francisco"
```

---

## 🔄 Data Collected

### Current Weather
- Temp, feels_like, pressure, humidity
- Weather main/description
- Wind, cloudiness, sunrise/sunset

### Forecast (5 days / 3-hour)
- 40 datapoints per city
- Temp, humidity, rain/snow 3h, weather, etc.

### Air Pollution
- AQI (1–5), PM2.5, PM10, CO, O3, NO2, SO2, NH3

---

## 📊 Recommended Use Cases
- Build dashboards in Excel or Tableau
- Analyze weather trends and patterns
- Compare pollution across cities
- Automate daily/weekly data pulls for time-series analysis

---

## 📁 Sample Cities (You Can Use Any)
- London, New York, Tokyo, Mumbai, Sydney, Dubai, Moscow, Cape Town, Toronto, São Paulo

---

## 📋 License
MIT License

---

_Weather data provided by [OpenWeatherMap](https://openweathermap.org/api)_

