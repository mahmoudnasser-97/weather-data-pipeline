import pandas as pd
import json
import os
import glob
import sys # New: to exit if data is bad

def transform_data():
    # 1. Find the newest file
    list_of_files = glob.glob('data/bronze/*.json')
    if not list_of_files:
        print("❌ No raw data found!")
        sys.exit(1) # Stop the script with an error
        
    latest_file = max(list_of_files, key=os.path.getctime)
    
    with open(latest_file, 'r') as f:
        data = json.load(f)
    
    # 2. Extract and Flatten
    clean_data = {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "temp_celsius": data.get("main", {}).get("temp"),
        "humidity": data.get("main", {}).get("humidity"),
        "weather_description": data["weather"][0]["description"] if data.get("weather") else None,
        "timestamp": data.get("dt")
    }
    
    # --- NEW: DATA QUALITY CHECKS ---
    print(f"Checking data quality for {latest_file}...")
    
    # Check 1: Is the temperature a reasonable number?
    if clean_data["temp_celsius"] is None or not (-60 <= clean_data["temp_celsius"] <= 60):
        print(f"⚠️ Alert! Unusual temperature detected: {clean_data['temp_celsius']}")
        sys.exit(1) # Stop! Don't load this into Gold.

    # Check 2: Is the city name missing?
    if not clean_data["city"]:
        print("⚠️ Alert! Missing city name.")
        sys.exit(1)

    print("✅ Data Quality Check Passed!")
    
    # 3. Save to Silver
    df = pd.DataFrame([clean_data])
    os.makedirs("data/silver", exist_ok=True)
    df.to_csv("data/silver/weather_cleaned.csv", index=False)
    print(f"✨ Cleaned data saved to Silver.")

if __name__ == "__main__":
    transform_data()