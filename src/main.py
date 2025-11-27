from flask import Flask, render_template, request
from process_data import ler_arquivo, validar_dados
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    arquivo = request.files["arquivo"]

    caminho = "data/upload.xlsx"
    arquivo.save(caminho)

    df = ler_arquivo(caminho)
    validacao = validar_dados(df)

    return f"<h1>Arquivo processado!</h1><p>{validacao}</p><pre>{df}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
