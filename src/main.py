from flask import Flask, render_template, request
import os
from process_data import ler_arquivo, validar_dados

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        arquivo = request.files.get("arquivo")

        if not arquivo:
            resultado = "Nenhum arquivo enviado."
        else:
            # Verifica extensão
            if not arquivo.filename.endswith(".csv"):
                resultado = "Envie um arquivo CSV válido!"
            else:
                caminho_salvo = os.path.join("data", "notas.csv")
                arquivo.save(caminho_salvo)

                df = ler_arquivo(caminho_salvo)
                resultado = validar_dados(df)

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
