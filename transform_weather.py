import pandas as pd
import json
import os
import glob

def transform_data():
    # 1. Find the newest file in the bronze folder
    list_of_files = glob.glob('data/bronze/*.json')
    if not list_of_files:
        print("No raw data found to transform!")
        return
        
    latest_file = max(list_of_files, key=os.path.getctime)
    
    # 2. Open the JSON file
    with open(latest_file, 'r') as f:
        data = json.load(f)
    
    # 3. "Flatten" the data into a simple dictionary
    # We only pick what we need for a clean table
    clean_data = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp_celsius": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_description": data["weather"][0]["description"],
        "timestamp": data["dt"] # This is 'Unix' time
    }
    
    # 4. Use Pandas to turn it into a Table (DataFrame)
    df = pd.DataFrame([clean_data])
    
    # 5. Save it to the Silver folder as a CSV
    os.makedirs("data/silver", exist_ok=True)
    df.to_csv("data/silver/weather_cleaned.csv", index=False)
    print(f"✨ Transformation complete! Cleaned data saved to Silver.")

if __name__ == "__main__":
    transform_data()