import sqlite3
from faker import Faker
import random

fake = Faker('pt_BR')

# Conectar ou criar banco
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS titulos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        secao TEXT NOT NULL,
        titulo TEXT NOT NULL
    )
''')

# Limpar dados anteriores
cursor.execute('DELETE FROM titulos')

# Gerar nomes únicos
nomes = set()
while len(nomes) < 250:
    nomes.add(fake.name())

secoes = ['101', '102']  # 2 seções diferentes

for nome in nomes:
    for secao in secoes:
        for i in range(4):  # 4 títulos por seção
            letra = fake.random_uppercase_letter()
            numero = random.randint(1, 999)
            titulo = f'Título {letra}{numero}'
            cursor.execute('INSERT INTO titulos (nome, secao, titulo) VALUES (?, ?, ?)', (nome, secao, titulo))

# Salvar e fechar
conn.commit()
conn.close()

print("Banco populado com 250 nomes, 2 seções, 4 títulos cada.")
