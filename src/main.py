from flask import Flask, render_template, request
from process_data import ler_arquivo, validar_dados
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "arquivo" not in request.files:
        return render_template("index.html", resultado="Erro: Nenhum arquivo enviado.")

    arquivo = request.files["arquivo"]

    if arquivo.filename == "":
        return render_template("index.html", resultado="Erro: Nome de arquivo inválido.")

    # Caminho temporário
    caminho_temp = "data/temp.xlsx"
    arquivo.save(caminho_temp)

    try:
        df = ler_arquivo(caminho_temp)
        validar = validar_dados(df)
        os.remove(caminho_temp)

        return render_template("index.html", resultado=f"Arquivo válido!\n\n{df.head()}")
    except Exception as e:
        return render_template("index.html", resultado=f"Erro ao processar: {e}")

if __name__ == "__main__":
    app.run(debug=True)
