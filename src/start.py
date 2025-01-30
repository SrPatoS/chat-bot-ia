import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from handler.climate_handler import climate_handler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /hello para receber uma saudação, /info para saber mais sobre o bot ou /clima Capitão Poço para verificar o clima de uma cidade")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Eu sou um bot simples feito para interações com usuários. Diga olá com /hello.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("oi", hello))
app.add_handler(CommandHandler("ajuda", help))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("clima", climate_handler))

app.run_polling()
