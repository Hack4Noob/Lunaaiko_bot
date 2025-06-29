
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Ayumi está viva 💘"

def run():
    app.run(host='0.0.0.0', port=5000)

def iniciar_servidor():
    Thread(target=run).start()
