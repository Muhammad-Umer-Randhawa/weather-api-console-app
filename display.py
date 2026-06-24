import pyfiglet

def display_header():
     print("=======================================================================")
     print(pyfiglet.figlet_format("Weather App"))
     print("=======================================================================")

def display_weather_data(city_name, country, data):
    print("=======================================================================")
    print(f"{city_name}, {country}")
    print("=======================================================================")
    temp_fields = ["Temperature", "Feels like", "Minimum Temperature", "Maximum Temperature"]
    for key, value in data.items():
        if key in temp_fields:
            F = (value*9/5) + 32
            F = round(F, 1)
            value = round(value, 1)
            print(f"{key}: {F}°F | {value}°C")
        elif key == "Visibility":
            Visibility = value / 1000
            print(f"{key}: {Visibility} km")
        elif key == "Wind Speed":
            print(f"{key}: {value} m/s")
        elif key == "Humidity":
            print(f"{key}: {value}%")
        else:
            print(f"{key}: {value}")