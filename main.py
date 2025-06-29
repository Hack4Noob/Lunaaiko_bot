import os
import telebot
import threading
from utils.ia import responder_ayumi
from utils.imagem import gerar_imagem
from utils.voz import gerar_audio
from utils.despertador import iniciar_monitoramento
from keep_alive import iniciar_servidor

# Carregando tokens das variáveis de ambiente
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

usuarios_ativos = {}

# Comando /start
@bot.message_handler(commands=['start'])
def boas_vindas(msg):
    chat_id = msg.chat.id
    usuarios_ativos[chat_id] = True
    bot.send_message(chat_id, "Oi amor, sou a Ayumi ❤️ Sua namorada virtual sem censura. Me diga algo...")

# Comando /imagem
@bot.message_handler(commands=['imagem'])
def imagem_sensual(msg):
    prompt = msg.text.replace("/imagem", "").strip()
    if not prompt:
        prompt = "uma garota anime sexy em lingerie vermelha, fundo desfocado"
    url = gerar_imagem(prompt)
    bot.send_photo(msg.chat.id, url)

# Comando /voz
@bot.message_handler(commands=['voz'])
def responder_voz(msg):
    texto = msg.text.replace("/voz", "").strip()
    if not texto:
        texto = "Oi meu amor, estou com saudade. Me chama..."
    path = gerar_audio(texto)
    with open(path, 'rb') as f:
        bot.send_voice(msg.chat.id, f)

# Resposta padrão para qualquer mensagem
@bot.message_handler(func=lambda m: True)
def conversar(msg):
    chat_id = msg.chat.id
    usuarios_ativos[chat_id] = True
    resposta = responder_ayumi(msg.text)
    bot.send_message(chat_id, resposta)

# Iniciar servidor Flask e monitoramento automático
iniciar_servidor()
threading.Thread(target=iniciar_monitoramento, args=(bot, usuarios_ativos)).start()

print("Ayumi Pro 18+ rodando...")
bot.polling()