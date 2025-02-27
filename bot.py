from dotenv import load_dotenv
import os
import requests
from telegram import Bot
import datetime


load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def get_weather(lat,long):
    params = {
        'lat' : lat,
        'lon' : long,
        'appid' : WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'es'  
    }

    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def string_format(weather_data):
    # Extraer datos relevantes
    city = "El Vedat, Alberic"
    weather = weather_data['weather'][0]['description']
    temp = round(weather_data['main']['temp'], 1)  # Redondear a 1 decimal
    feels_like = round(weather_data['main']['feels_like'], 1)  # Sensación térmica
    humidity = weather_data['main']['humidity']  # Humedad
    wind_speed = weather_data['wind']['speed']  # Velocidad del viento

    # Crear el string formateado
    weather_info = (
        f"🌍 Ciudad: {city}\n"
        f"🌤 Clima: {weather.capitalize()}\n"
        f"🌡 Temperatura: {temp}°C\n"
        f"🤔 Sensación térmica: {feels_like}°C\n"
        f"💧 Humedad: {humidity}%\n"
        f"🌬 Viento: {wind_speed} m/s\n"
        f"Hora: {datetime.datetime.now().strftime('%H:%M:%S')}\n"
    )
    return weather_info

def send_message(chat_id,text):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')

if __name__ == '__main__':
    weather_data = get_weather(-34.6132,-58.3772)
    if weather_data:
        weather_info = string_format(weather_data)
        send_message(TELEGRAM_BOT_TOKEN,weather_info)
    else:
        send_message(TELEGRAM_BOT_TOKEN,"No se pudo obtener la información del clima")