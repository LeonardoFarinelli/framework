from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cad/usuario")
def usuario():
    return render_template('cadusuario.html')

@app.route("/cad/anuncio")
def anuncio():
    return render_template('cadanuncio.html')

@app.route("/anuncios/pergunta")
def pergunta():
    return render_template('pergunta.html')

@app.route("/anuncios/compra")
def compra():
    return render_template('compra.html')

@app.route("/anuncios/favoritos")
def favoritos():
    return render_template('favoritos.html')

@app.route("/config/categoria")
def categoria():
    return render_template('configcat.html')

@app.route("/relatorios/vendas")
def vendas():
    return render_template('relvendas.html')

@app.route("/relatorios/compras")
def compras():
    return render_template('relcompras.html')
