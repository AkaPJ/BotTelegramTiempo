from bot import get_weather, string_format
from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio
import datetime

load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def enviar_clima():
    bot = Bot(TELEGRAM_BOT_TOKEN)
    
    payload = string_format(get_weather(39.1336826,-0.5705442))
    
    await bot.send_message(chat_id=CHAT_ID, text=payload, parse_mode='Markdown')


async def programar_envios():
    while True:
        ahora = datetime.datetime.now()
        # Define las horas de envío (por ejemplo, 8:00 AM y 8:00 PM)
        proximos_envios = [
            ahora.replace(hour=16, minute=8, second=0, microsecond=0),
            ahora.replace(hour=16, minute=9, second=0, microsecond=0),
        ]
        # Encuentra el próximo envío
        tiempo_restante = min((hora - ahora).total_seconds() for hora in proximos_envios if hora > ahora)
        if tiempo_restante < 0:
            tiempo_restante += 86400  # Añade 24 horas si ya pasó el tiempo
        print(f"Próximo envío en {tiempo_restante // 3600} horas")
        await asyncio.sleep(tiempo_restante)  # Espera hasta el siguiente envío
        await enviar_clima()

asyncio.run(programar_envios())