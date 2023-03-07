import sqlite3 as sql

conexao = sql.connect('signos.bd')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS "signo" (
    nome TEXT,
    descricao TEXT,
    data INTEGER
    '''
)

