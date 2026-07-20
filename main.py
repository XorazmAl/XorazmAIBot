import os
import telebot
from flask import Flask
from threading import Thread
AAPI_TOKEN = 8860187470:AAFQj-YRPF2dv03rzrviVvkwEkOo5seJkLsos.getenv("BOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men ishlayapman.")

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    Thread(target=run).start()
    bot.infinity_polling()
