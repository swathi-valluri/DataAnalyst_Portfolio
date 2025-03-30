# 📘 Weather Data Tracker

This project allows you to fetch, export, and visualize weather data (current, forecast, and pollution) for multiple cities using the **OpenWeatherMap API**.

Built for data analysis, this tool helps you:
- Fetch clean weather data
- Export it to Excel
- Auto-generate per-city weather charts

---

## 📦 Features

✅ Fetch **Current Weather**  
✅ Fetch **5-Day Weather Forecast**  
✅ Fetch **Air Pollution Data (AQI & PM2.5)**  
✅ Export all data to a single **Excel workbook**  
✅ Auto-generate **static PNG charts per city**  
✅ Accept multiple city inputs via CLI  
✅ Modular fetcher, visualizer, and reporter structure

---

## 📁 Project Structure

```
weather-data-tracker/
├── charts/                     # 📊 Generated charts (1 PNG per city)
├── exports/                    # 📄 Excel files containing weather data
├── src/
│   ├── fetch_current.py        # API call for current weather
│   ├── fetch_forecast.py       # API call for 5-day forecast
│   ├── fetch_pollution.py      # API call for pollution (AQI)
│   ├── geocode.py              # Fetch latitude/longitude
│   ├── visualizer.py           # Chart generation logic
│   ├── config.py               # API key + environment loader
│   ├── database.py             # (Optional) For future database integration
│   └── reporter.py             # Excel file writer
├── test/                       # Unit tests for each module
│   ├── test_current.py
│   ├── test_forecast.py
│   └── test_pollution.py
├── main.py                     # 🔁 CLI to fetch + export + visualize
├── pyproject.toml              # Poetry project file
├── .env                        # API key storage
```

---

## 🔧 Setup Instructions

### 1️⃣ Install Poetry & Dependencies

```bash
poetry install
```

### 2️⃣ Create `.env` File

```env
API_KEY=your_openweathermap_api_key_here
```

---

## 🚀 How to Use

### ▶️ Run from terminal (Poetry shell)

```bash
poetry shell
python main.py --type all
```

It will prompt:

```bash
🌍 Enter city names separated by comma:
> london, new york, tokyo
```

### What It Does:
- Fetches current, forecast, and pollution data
- Saves Excel file to: `exports/weather_data_combined_<timestamp>.xlsx`
- Generates charts per city and saves to: `charts/`

---

## 📊 Output Samples

### Excel:
- Sheet 1: **Current Weather**
- Sheet 2: **Forecast**
- Sheet 3: **Pollution**

### Charts:
- Temp + Humidity over 5 days
- Rain + Snow bar plot
- AQI + PM2.5 bar chart

Each chart saved as:
```
charts/london_weather_chart.png
charts/new_york_weather_chart.png
...
```

---

## 🧪 Run Tests

```bash
python test/test_current.py
python test/test_forecast.py
python test/test_pollution.py
```

---

## 📌 Requirements

- Python 3.9+
- OpenWeatherMap Free API Key
- Dependencies managed by Poetry

---

## 🧠 Future Ideas (Optional Add-ons)

| Feature | Tool | Benefit |
|--------|------|---------|
| Dashboard UI | Streamlit | Interactive web display |
| Chart to PDF | `reportlab`, `fpdf` | Shareable reports |
| SQLite Logger | `sqlite3`, `sqlalchemy` | Store daily logs for historical tracking |
| Interactive Charts | `plotly`, `altair` | Zoom, hover, tooltips |

---

## 📝 License

This project is licensed under the MIT License.

---
