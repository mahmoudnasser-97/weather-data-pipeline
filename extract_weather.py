import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Cairo"

def fetch_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # --- NEW LOGIC: DATA VERSIONING ---
        # 1. Create a unique filename using the current date and time
        # Format: 2024-05-20_14-30-05.json
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"weather_{CITY}_{timestamp}.json"
        
        # 2. Define the path to the Bronze folder
        folder_path = "data/bronze"
        
        # 3. Create the folder if it doesn't exist (safety check)
        os.makedirs(folder_path, exist_ok=True)
        
        # 4. Save the file into the Bronze folder
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
            
        print(f"✅ Success! Raw data saved to: {file_path}")
    else:
        print(f"❌ Failed to fetch data. Error: {response.status_code}")

if __name__ == "__main__":
    fetch_weather_data()