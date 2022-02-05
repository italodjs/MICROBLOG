from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = "Italo de Jesus Souza"
    return render_template('index.html', nome=nome)

@app.route('/contato')
def contato():
    Email = 'italodjs@live.com'
    Telefone = '(71) 9 8833-3504'
    Cidade = 'Salvador'
    return render_template('contato.html', email = Email, telefone = Telefone, cidade = Cidade)