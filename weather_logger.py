import requests
import csv
from datetime import datetime
import os

# --- YOUR SETTINGS ---
API_KEY = "a0d500babadccb4a52946558e5f00326"
CITY_1 = "Columbia,MD,US"
CITY_2 = "Baltimore,MD,US"
FILE_NAME = "science_project_weather.csv"

def get_temperature(city_name):
    """Fetches ONLY the temperature for a given city from the API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=imperial"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Digging into the data to pull out just the temperature
        temp = data['main']['temp']
        return temp
        
    except Exception as e:
        print(f"Error getting weather for {city_name}: {e}")
        return "Error"

def save_to_spreadsheet(temp_1, temp_2):
    """Saves both temperatures side-by-side in the CSV file."""
    
    # Check if the file already exists
    file_exists = os.path.isfile(FILE_NAME)
    
    # Open the file in 'a' (append) mode to add a new line
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If it's a brand new file, write the custom column headers first
        if not file_exists:
            writer.writerow(["Time", f"{CITY_1} Temp (F)", f"{CITY_2} Temp (F)"])
            
        # Get the exact time right now
        now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        
        # Write the time and both temperatures into a single row
        writer.writerow([now, temp_1, temp_2])
        print(f"Success! Logged {CITY_1}: {temp_1}°F and {CITY_2}: {temp_2}°F at {now}")

# --- RUN THE PROGRAM ---
if __name__ == "__main__":
    # Get the temp for the first city
    current_temp_1 = get_temperature(CITY_1)
    
    # Get the temp for the second city
    current_temp_2 = get_temperature(CITY_2)
    
    # Save them both to the file
    save_to_spreadsheet(current_temp_1, current_temp_2)