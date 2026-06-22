import re

pattern = "^[a-zA-Z- ]+$"
def get_city():
    while True:
        city_name = input("Enter the city name to know its forecast: ")
        clear_name = " ".join(city_name.split()).lower().title()
        if clear_name == "":
            print("You have to enter a city name.")
            continue
        result = re.match(pattern, clear_name)
        if result == None:
            print("Invalid city name, enter again")
            continue
        else:
            return clear_name

if __name__ == "__main__":
    print(get_city())