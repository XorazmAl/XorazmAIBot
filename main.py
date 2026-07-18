import os
from flask import Flask
from threading import Thread

# Web server yaratamiz (Render o'chirmasligi uchun)
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot ishlayapti!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Botni ishga tushiramiz
def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()

#!/usr/bin/env python
os.environ.get('API_TOKEN')
