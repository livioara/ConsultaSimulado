from flask import Flask, render_template, request
import sqlite3
from flask import jsonify

app = Flask(__name__)

def buscar_titulos(nome, secao):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT titulo FROM titulos WHERE nome = ? AND secao = ?", (nome, secao))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    nome = request.form['nome']
    secao = request.form['secao']
    resultados = buscar_titulos(nome, secao)
    if resultados:
        return render_template('index.html', resultados=resultados, nome=nome, secao=secao)
    else:
        mensagem = "Nenhum título encontrado para os critérios informados."
        return render_template('index.html', mensagem=mensagem, nome=nome, secao=secao)
    
@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('query', '')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT nome FROM titulos WHERE nome LIKE ? LIMIT 10", (f'{query}%',))
    nomes = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify(sugestoes=nomes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
