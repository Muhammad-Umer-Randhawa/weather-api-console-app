from input_validate import get_city
from city_selector import get_coordinates
from api_handler import get_weather
from display import display_weather_data
from display import display_header

def main():
    display_header()
    city_name = get_city()
    result = get_coordinates(city_name)  
    if result is None:                    
        print("City not found")
        return             
    lat, lon, name, country = result    
    data = get_weather(lat, lon)
    display_weather_data(name, country, data)
    
if __name__ == "__main__":
    main()