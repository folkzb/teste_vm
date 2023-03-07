from datetime import date
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3 as sql

from flask import Flask,request
#import mysql.connector as sql

app = Flask(__name__)
banco = 'signos.db'

def abrir_conexao(banco):
    conexao = sql.connect(banco)
    cursor = conexao.cursor()
    return conexao, cursor

def fechar_conexao(conexao):
    conexao.commit()
    conexao.close()

today = date.today()

# Comandos SQL
contagem = "SELECT COUNT(*) FROM signo;"
select_todos = "SELECT * FROM signo;"
truncate = "TRUNCATE TABLE signo;"
select_dia="SELECT * FROM signo WHERE dia like ?"

conexao, cursor = abrir_conexao(banco)
cursor.execute(select_dia, [today])
day = cursor.fetchone()
conexao.close()
#fechar_conexao(conexao)



select_nome = "SELECT * FROM signo WHERE nome like ?"
delete_nome = "DELETE FROM signo WHERE nome like ?"
insert = "INSERT INTO signo VALUES :descricao"
update ='''
UPDATE signo SET
    descricao = :descricao,
    dia = :dia
WHERE nome like :nome
'''

options = webdriver.ChromeOptions()##executar hidden
options.add_argument("--headless")#executar hidden
driver = webdriver.Chrome(executable_path='/home/folkz/Desktop/signo/chromedriver',chrome_options=options)

signos = ['aries', 'touro', 'gemeos', 'cancer', 'leao', 'virgem', 'libra', 'escorpiao', 'sagitario', 'capricornio', 'aquario', 'peixes']

if day != today:
    for signo in signos:
        driver.get(f'https://www.personare.com.br/horoscopo-do-dia/{signo}')
        sleep(2)
        rows = driver.find_elements(By.XPATH, '/html/body/main/div/div/div[1]/div/div[1]/div[1]/p')
        for row in rows:
            descricao=(row.text)
            if signo == 'aries':
                aries={"nome":"aries","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, aries)
                fechar_conexao(conexao)
            elif signo == 'touro':
                touro={"nome":"touro","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, touro)
                fechar_conexao(conexao)
            elif signo == 'gemeos':
                gemeos={"nome":"gemeos","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, gemeos)
                fechar_conexao(conexao)
            elif signo == 'cancer':
                cancer={"nome":"cancer","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, cancer)
                fechar_conexao(conexao)
            elif signo == 'leao':
                leao={"nome":"leao","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, leao)
                fechar_conexao(conexao)
            elif signo == 'virgem':
                virgem={"nome":"virgem","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, virgem)
                fechar_conexao(conexao)
            elif signo == 'libra':
                libra={"nome":"libra","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, libra)
                fechar_conexao(conexao)
            elif signo == 'escorpiao':
                escorpiao={"nome":"escorpiao","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, touro)
                fechar_conexao(conexao)
            elif signo == 'gemeos':
                gemeos={"nome":"gemeos","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, gemeos)
                fechar_conexao(conexao)
            elif signo == 'sagitario':
                sagitario={"nome":"sagitario","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, sagitario)
                fechar_conexao(conexao)
            elif signo == 'capricornio':
                capricornio={"nome":"capricornio","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, capricornio)
                fechar_conexao(conexao)
            elif signo == 'aquario':
                aquario={"nome":"aquario","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, aquario)
                fechar_conexao(conexao)
            elif signo == 'peixes':
                peixes={"nome":"peixes","descricao":descricao,"dia":today}
                conexao, cursor = abrir_conexao(banco)
                cursor.execute(update, peixes)
                fechar_conexao(conexao)
            else:
                pass
else:
    pass

@app.route('/signo/<signonome>')
def index(signonome):
    conexao, cursor = abrir_conexao(banco)
    cursor.execute(select_nome, [signonome])
    resultado = cursor.fetchall()
    fechar_conexao(conexao)
    return resultado


if __name__ == "__main__":
    app.run()
