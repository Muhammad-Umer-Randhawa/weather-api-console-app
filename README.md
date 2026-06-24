# Weather API Console App

A simple Python CLI tool that fetches and displays current weather forecasts using the [OpenWeatherMap API](https://openweathermap.org/). It handles duplicate city matches (letting you choose the correct location) and formats the output into a clean, easy-to-read console display.

## Features

- **Accurate Coordinates**: Uses OpenWeather's Geocoding API to convert city names to latitude and longitude.
- **Duplicate Handling**: If you search for a city that exists in multiple states or countries (like London or Springfield), the app lists up it's matches and lets you choose the correct one.
- **Detailed Forecast**: Shows temperature (in both °C and °F), feels-like temp, min/max range, sky conditions, humidity, visibility, and wind speed.
- **Local Sunrise & Sunset**: Sunrise and sunset times are automatically adjusted to the local timezone of the queried city, not your system's timezone.
- **ASCII Art Header**: Uses `pyfiglet` to show a simple CLI title header.

## Setup & Installation

### 1. Clone the project and navigate to the directory
```bash
git clone <repository-url>
cd "weather-api-console-app"
```

### 2. Install dependencies
Make sure you have Python installed (version 3.11.9), then install the required packages:
```bash
pip install -r requirements.txt
```
*(Dependencies: `requests`, `python-dotenv`, and `pyfiglet`)*

### 3. Get an OpenWeather API Key
1. Go to [OpenWeatherMap](https://openweathermap.org/) and sign up for a free account.
2. Generate an API Key (typically the standard "Current Weather Data" / "Geocoding API" subscription which is free).

### 4. Configure Environment Variables
Create a file named `.env` in the root directory of the project and add your API key:
```env
OPENWEATHER_API_KEY=your_actual_api_key_here
```

## How to Run

Simply run the `main.py` script:
```bash
python main.py
```

### Example Usage:
1. Run the script.
2. Enter the city name (e.g., `Paris`).
3. If there are multiple matches, choose the correct one from the list (e.g., entering `1` for Paris, France).
4. View the current weather statistics.

## Project Structure

- `main.py` — The main entry point of the app. It coordinates the inputs, API calls, and outputs.
- `input_validate.py` — Sanitizes user input to ensure the city name only contains letters, spaces, and hyphens before making requests.
- `city_selector.py` — Queries the Geocoding API. If multiple cities match, it displays them and prompts you to select one.
- `api_handler.py` — Fetches current weather data for the selected coordinates and processes the response.
- `display.py` — Formats and prints the weather data.
