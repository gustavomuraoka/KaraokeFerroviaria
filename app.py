from flask import Flask  #Importa a classe flask

app = Flask("__name__")  #Cria uma instância dessa classe

@app.route("/")  #Criando rotas com decorador

def hello_world():  #Funlção para retornar uma mensagem

    return "<p>Hello, Flask!</p>"