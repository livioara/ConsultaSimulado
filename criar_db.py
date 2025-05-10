import sqlite3
import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('data/titulos.csv')
print(df.columns)


# Cria banco SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Cria tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS titulos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        secao TEXT NOT NULL,
        titulo TEXT NOT NULL
    )
''')

# Insere dados
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO titulos (nome, secao, titulo)
        VALUES (?, ?, ?)
    ''', (row['nome'], row['secao'], row['titulo']))

conn.commit()
conn.close()

print("Banco de dados criado e populado com sucesso.")
