from dotenv import load_dotenv
import os
import requests

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def get_weather(lat,long):
    params = {
        'lat' : lat,
        'lon' : long,
        'appid' : WEATHER_API_KEY
    }

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def string_format(weather_data):
    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']
    temp = temp - 273.15
    temp = round(temp, 2)
    return f"Temps actual: {weather}, Temperatura: {temp}°C"

print(string_format(get_weather(41.3887901,2.1589899)))