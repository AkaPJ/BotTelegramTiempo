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


asyncio.run(enviar_clima())