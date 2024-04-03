import unidecode
from flask import Flask, render_template, request  #Importa a classe flask

app = Flask("__name__")  #Cria uma instância dessa classe

with open("static/Musicas.txt", "r", encoding="utf-8") as musicas:
    musicas_Ids = musicas.readlines()


@app.route("/", methods = ['GET', 'POST'])  #Criando rotas com decorador
def home():  #Função para retornar uma mensagem

    if request.method == 'POST':
        pesquisa_input = request.form['musica']
        musicas_pesquisa = requestMusic(pesquisa_input)
        if len(musicas_pesquisa) == 0: musicas_pesquisa.append("Música não encontrada")
        return render_template("index.html", len = len(musicas_pesquisa), musicas_Ids = musicas_pesquisa)

    return render_template("index.html", len = len(musicas_Ids), musicas_Ids = musicas_Ids)




def requestMusic(pesquisa_input):

    resultado_output = []
    for i in musicas_Ids:
        if unidecode.unidecode(pesquisa_input.lower()) in unidecode.unidecode(i.lower()):
            resultado_output.append(i)
            
    return resultado_output


if __name__ == '__main__':
    app.run(debug=True)