import os
import openai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# .env fayldan token va API kalitlarni yuklash
load_dotenv()
TELEGRAM_TOKEN = os.getenv("7505715870:AAEopIKBJcfbW3mvpS6vZ7_BnfesoSFN_PQ")
OPENAI_API_KEY = os.getenv("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")

openai.api_key = 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

# Start komandasi uchun javob
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Men Yurist AI botman. Yuridik savolingizni yozing.")

# Matnli xabarlarga javob
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # OpenAI javobini olish
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # agar sizda GPT-4 bo‘lsa, shu yerda almashtirishingiz mumkin
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response["choices"][0]["message"]["content"]
    await update.message.reply_text(bot_reply)

# Botni ishga tushirish
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()
