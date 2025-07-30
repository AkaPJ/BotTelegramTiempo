from dotenv import load_dotenv
import os
import requests
from telegram import Bot
import asyncio
import datetime
import zoneinfo


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
    wind_speed = round(wind_speed * 3.6,2)

    # Crear el string formateado
    weather_info = (
        f"🌍 Ciudad: {city}\n"
        f"🌤 Clima: {weather.capitalize()}\n"
        f"🌡 Temperatura: {temp}°C\n"
        f"🤔 Sensación térmica: {feels_like}°C\n"
        f"💧 Humedad: {humidity}%\n"
        f"🌬 Viento: {wind_speed} km/h\n"
        f"Hora: {datetime.datetime.now(zoneinfo.ZoneInfo('Europe/Madrid')).strftime('%H:%M:%S')}\n"
    )
    return weather_info

CHAT_ID = os.getenv("CHAT_ID")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def enviar_clima():
    bot = Bot(TELEGRAM_BOT_TOKEN)
    
    payload = string_format(get_weather(39.1336826,-0.5705442))
    
    await bot.send_message(chat_id=CHAT_ID, text=payload, parse_mode='Markdown')


asyncio.run(enviar_clima())