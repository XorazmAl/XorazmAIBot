i
   import os
import telebot
from flask import Flask
from threading import Thread

# Tokeningizni mana bu yerga, tirnoq ichiga yozing
API_TOKEN = '8860187470:AAGge6qQ95Fa9GzmEt-BgudJ4-d'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men ishlayapman.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
