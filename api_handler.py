import requests
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import os
def get_weather(lat, lon):
    try:
        load_dotenv()
        key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}"
        response = requests.get(url)
        data = response.json()
        tz = timezone(timedelta(seconds=data["timezone"]))
        if(data["cod"] == 200):
            return {
                "Temperature" : data["main"]["temp"],
                "Feels like" : data["main"]["feels_like"],
                "Minimum Temperature" : data["main"]["temp_min"],
                "Maximum Temperature" : data["main"]["temp_max"],
                "Sky" : data["weather"][0]["description"],
                "Humidity" : data["main"]["humidity"],
                "Visibility" :  data["visibility"],
                "Wind Speed" : data["wind"]["speed"],
                "Sunrise" : datetime.fromtimestamp(data["sys"]["sunrise"], tz = tz).strftime("%I:%M %p"),
                "Sunset" : datetime.fromtimestamp(data["sys"]["sunset"], tz = tz).strftime("%I:%M %p")
            }
        else:
            print("Unable to fetch weather data, please try again later")
            return None
    except requests.exceptions.ConnectionError:
        print("Unable to fetch weather data, please try again later")
        return None
