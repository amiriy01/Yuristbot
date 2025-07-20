import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("7505715870:AAFpsMimSyhB9rOd4CzqEAyGI7GdvOoD2u8")
OPENAI_API_KEY = os.getenv("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")

openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Yuridik yoki boshqa savolingiz bo‘lsa, yozing.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response['choices'][0]['message']['content']
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text("Xatolik: " + str(e))

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot ishga tushdi...")
    app.run_polling()
