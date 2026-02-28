import os
import requests
import json
from dotenv import load_dotenv

# 1. Load the secret key from our .env file
load_dotenv()
API_KEY = os.getenv("05319863fbf64b63685c18b497163508")

# 2. Define the city we want to track (You can change this to Cairo or London!)
CITY = "Cairo"
URL = f"https://api.openweathermap.org/data/2.5/weather?q=Cairo&appid=05319863fbf64b63685c18b497163508&units=metric"

def fetch_weather_data():
    # 3. Ask the internet for the data
    response = requests.get(URL)
    
    # 4. Check if the connection worked (Status 200 means "OK")
    if response.status_code == 200:
        data = response.json()
        print(f"Successfully fetched data for Cairo!")
        
        # 5. Save this "Raw" data to a file so we don't lose it
        with open("raw_weather_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved to raw_weather_data.json")
    else:
        print(f"Error: {response.status_code}")

# Run the function
if __name__ == "__main__":
    fetch_weather_data()