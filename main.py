import os
import openai
import telebot
from dotenv import 


BOT_TOKEN = os.getenv("7505715870:AAEopIKBJcfbW3mvpS6vZ7_BnfesoSFN_PQ")
OPENAI_API_KEY = os.getenv("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")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "🧑‍⚖️ Salom! Men Yurist Botman. Menga yuridik savollar bering, men javob beraman."
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = f"Sen O'zbekiston qonunlariga asoslangan yuristsan. Quyidagi savolga yuridik asosda, tushunarli qilib javob ber:\n\n{message.text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response['choices'][0]['message']['content']
    bot.send_message(message.chat.id, reply)

bot.polling()
