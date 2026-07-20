import os
import telebot
from flask import Flask
from threading import Thread
from openai import OpenAI

# Telegram Bot Token
API_TOKEN = "8860187470:AAGtpaZRBVqg3ujsGEEl7pPg6J5P4vbG680"

bot = telebot.TeleBot(API_TOKEN)

# OpenAI API Key (Render Environment Variables)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return "XorazmAI ishlayapti!"

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 Assalomu alaykum!\nMen XorazmAI. Savolingizni yozing."
    )

@bot.message_handler(func=lambda m: True)
def chat(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Sen XorazmAI nomli foydali va muloyim Telegram yordamchisisan."
                },
                {
                    "role": "user",
                    "content": message.text
                }
            ]
        )

        bot.reply_to(message, response.choices[0].message.content)

    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.infinity_polling(skip_pending=True)
