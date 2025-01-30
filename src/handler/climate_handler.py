import os

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

async def climate_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if context.args:
            city = " ".join(context.args)
        else:
            await update.message.reply_text("❌ Você precisa informar uma cidade. Exemplo: /clima Capitão Poço")
            return

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=pt_br"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            await update.message.reply_text(f"🌤 Clima em {city}:\n🌡 Temperatura: {temp}°C\n☁️ Condição: {desc}")
        else:
            await update.message.reply_text(f"❌ Erro {response.status_code}: {data.get('message', 'Erro desconhecido')}")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Ocorreu um erro ao buscar o clima: {str(e)}")
