# 🌦️ Real-Time Weather Data Pipeline

An end-to-end Data Engineering pipeline that extracts weather data, cleans it using the Medallion Architecture, and stores it in a DuckDB Data Warehouse.

## 🏗️ Architecture
- **Bronze Layer**: Raw JSON data from OpenWeatherMap API (Versioned with timestamps).
- **Silver Layer**: Cleaned CSV data processed with Pandas.
- **Gold Layer**: Analytical Data Warehouse powered by DuckDB.

## 🛠️ Tech Stack
- **Python** (Requests, Pandas)
- **DuckDB** (OLAP Database)
- **GitHub Actions** (Coming soon: Automation)

## 🚀 How to Run
1. Clone the repo.
2. Add your `OPENWEATHER_API_KEY` to a `.env` file.
3. Run `python extract_weather.py`
4. Run `python transform_weather.py`
5. Run `python load_to_warehouse.py`