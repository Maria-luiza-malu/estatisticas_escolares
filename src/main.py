from flask import Flask, render_template, request, redirect, url_for
import os
from process_data import ler_arquivo, validar_dados, gerar_estatisticas, gerar_grafico


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        arquivo = request.files.get("arquivo")

        if not arquivo:
            return render_template("index.html", resultado="Nenhum arquivo enviado.")

        if not arquivo.filename.endswith(".csv"):
            return render_template("index.html", resultado="Envie um arquivo CSV válido!")

        # Salvar arquivo
        caminho_salvo = os.path.join(BASE_DIR, "data", "notas.csv")
        arquivo.save(caminho_salvo)

        # Ler arquivo
        df = ler_arquivo(caminho_salvo)
        validacao = validar_dados(df)

        if validacao != "Dados validados com sucesso!":
            return render_template("index.html", resultado=validacao)

        # Se validou tudo, redireciona para página de resultados
        return redirect(url_for("resultado"))

    return render_template("index.html")


@app.route("/resultado")
def resultado():
    caminho_salvo = os.path.join(BASE_DIR, "data", "notas.csv")
    df = ler_arquivo(caminho_salvo)

    estatisticas = gerar_estatisticas(df)

    # Transformar DataFrame em HTML bonitinho
    tabela_html = df.to_html(classes="tabela", index=False)

    return render_template("resultado.html", tabela=tabela_html, estatisticas=estatisticas)


if __name__ == "__main__":
    app.run(debug=True)
