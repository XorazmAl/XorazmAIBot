import os
import telebot
from flask import Flask
from threading import Thread

# Tokeningizni mana bu yerga joylang
API_TOKEN=8860187470:AAGge6qG95Fa9GzmEt-BgudJ4-d9fwoUQ8I


app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men ishlayapman.")

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == "__main__":
    Thread(target=run).start()
    bot.infinity_polling()

