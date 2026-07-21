import os
from threading import Thread
from flask import Flask
import telebot
from groq import Groq

BOT_TOKEN = os.getenv("BOT_TOKEN")"8860187470:AAGtpaZRBVqg3ujsGEEl7pPg6J5P4vbG680"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return "XorazmAI ishlayapti!"

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 Assalomu alaykum!\nMen XorazmAI.\nSavolingizni yozing."
    )

@bot.message_handler(func=lambda m: True)
def chat(message):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Sen XorazmAI nomli foydali o'zbek tilidagi yordamchisan."
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
