import os
import telebot
from flask import Flask
from threading import Thread
API_TOKEN = "8860187470:AAGzdkoyPt6DBj5HRj4Y77E8DShZtX_i5RM"
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
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
@bot.message_handler(func=lambda message: True)
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
