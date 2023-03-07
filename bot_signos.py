from datetime import date
from time import sleep

import telebot
import requests
from datetime import datetime

today = date.today()

signos = ['aries', 'touro', 'gemeos', 'cancer', 'leao', 'virgem', 'libra', 'escorpiao', 'sagitario', 'capricornio', 'aquario', 'peixes']

#telebot
TOKEN = "5504145559:AAEvF83NSceveBVHSVICvKmauY8NQup9VCQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["Aries"])
def ariesdef(mensagem):
    aries=requests.get('http://127.0.0.1:5000/signo/aries').json()
    messageText = f'{today} - ' + aries[0][1]
    bot.send_message(mensagem.chat.id, messageText)

@bot.message_handler(commands=["Touro"])
def tourodef(mensagem):
    touro=requests.get('http://127.0.0.1:5000/signo/touro').json()
    messageText = f'{today} - ' + touro[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Gemeos"])
def gemeosdef(mensagem):
    gemeos=requests.get('http://127.0.0.1:5000/signo/gemeos').json()
    messageText = f'{today} - ' + gemeos[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Cancer"])
def cancerdef(mensagem):
    cancer=requests.get('http://127.0.0.1:5000/signo/cancer').json()
    messageText = f'{today} - ' + cancer[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Leao"])
def leaodef(mensagem):
    leao=requests.get('http://127.0.0.1:5000/signo/leao').json()
    messageText = f'{today} - ' + leao[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Virgem"])
def virgemdef(mensagem):
    virgem=requests.get('http://127.0.0.1:5000/signo/virgem').json()
    messageText = f'{today} - ' + virgem[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Libra"])
def libradef(mensagem):
    libra=requests.get('http://127.0.0.1:5000/signo/libra').json()
    messageText = f'{today} - ' + libra[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Escorpiao"])
def escorpiaodef(mensagem):
    escorpiao=requests.get('http://127.0.0.1:5000/signo/escorpiao').json()
    messageText = f'{today} - ' + escorpiao[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Sagitario"])
def sagitariodef(mensagem):
    sagitario=requests.get('http://127.0.0.1:5000/signo/sagitario').json()
    messageText = f'{today} - ' + sagitario[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Capricornio"])
def capricorniodef(mensagem):
    capricornio=requests.get('http://127.0.0.1:5000/signo/touro').json()
    messageText = f'{today} - ' + capricornio[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Aquario"])
def aquariodef(mensagem):
    aquario=requests.get('http://127.0.0.1:5000/signo/aquario').json()
    messageText = f'{today} - ' + aquario[0][1]
    bot.send_message(mensagem.chat.id, messageText)
    
@bot.message_handler(commands=["Peixes"])
def peixesdef(mensagem):
    peixes=requests.get('http://127.0.0.1:5000/signo/peixes').json()
    messageText = f'{today} - ' + peixes[0][1]
    bot.send_message(mensagem.chat.id, messageText)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Selecione um signo
    /Aries
    /Touro
    /Gemeos
    /Cancer
    /Leao
    /Virgem
    /Libra
    /Escorpiao
    /Sagitario
    /Capricornio
    /Aquario
    /Peixes
    """
    bot.reply_to(mensagem, texto)

bot.polling()

