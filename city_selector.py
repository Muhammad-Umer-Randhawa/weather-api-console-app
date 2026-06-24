import requests
from dotenv import load_dotenv
import os
def get_coordinates(city_name):
    load_dotenv()
    key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={key}"
    response = requests.get(url)
    data = response.json()

    if len(data) == 0:
        return None
    elif len(data) == 1:
        return data[0]["lat"], data[0]["lon"], data[0]["name"], data[0]["country"]
    
    for i, city in enumerate(data):
        print(f"{i+1}. {city['name']}, {city.get('state', '')}, {city['country']}")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice > len(data):
                print("Enter a valid choice")
                continue
        except Exception as e:
            print("Enter a valid choice")
            continue
        selected = data[choice - 1]
        return selected["lat"], selected["lon"], selected["name"], selected["country"]