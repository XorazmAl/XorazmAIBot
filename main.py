import os
import telebot
from flask import Flask
from threading import Thread

# Botni aniqlash
API_TOKEN = 'SIZNING_TOKENINGIZNI_SHU_YERGA_YOZING'
bot = telebot.TeleBot(API_TOKEN)

# Veb-server qismi (Render uchun)
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# Bot komandalari
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men ishlayapman.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()


#!/usr/bin/env python
os.environ.get('API
