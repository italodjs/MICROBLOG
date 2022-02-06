import sqlite3
from app import app
from flask import render_template
from flask import request
import microblog


#=======================================BANCO DE DADOS===============================

conn = sqlite3.connect("microblog.db")
conn.row_factory = lambda cursor, row:row[0]
cursor = conn.cursor()
#Gab = cursor.execute('SELECT Gabinete from Cadastro').fetchall()



###########################################################################################

@app.route('/', defaults={"nome":"home"})
@app.route('/index', defaults={"nome":"usuário"})
@app.route('/index/<nome>')
def index(nome):
    return render_template('index.html', nome=nome)

@app.route('/contato')
def contato():
    Email = 'italodjs@live.com'
    Telefone = '(71) 9 8833-3504'
    Cidade = 'Salvador.'
    return render_template('contato.html', email = Email, telefone = Telefone, cidade = Cidade)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    Gab = cursor.execute('SELECT Nome from cadastro').fetchall()
    return "usuario {}, senha {}, {}".format(usuario, senha, Gab)