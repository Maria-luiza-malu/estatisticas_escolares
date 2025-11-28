import pandas as pd
import matplotlib.pyplot as plt
import os

def ler_arquivo(caminho_arquivo):
    encodings = ["utf-8", "latin-1", "iso-8859-1", "cp1252"]

    for enc in encodings:
        try:
            print(f"Tentando encoding: {enc}")
            df = pd.read_csv(caminho_arquivo, encoding=enc, sep=";")
            return df
        except Exception as e:
            print(f"Falhou com {enc}: {e}")

    return "Erro: não foi possível ler o CSV."


def validar_dados(df):
    if isinstance(df, str):
        return df  # já é mensagem de erro

    colunas_esperadas = ["aluno", "disciplina", "nota"]

    colunas_arquivo = df.columns.tolist()
    print("COLUNAS ENCONTRADAS:", colunas_arquivo)

    for col in colunas_esperadas:
        if col not in df.columns:
            return f"Erro: coluna obrigatória ausente → {col}"

    return "Dados validados com sucesso!"

def gerar_estatisticas(df):
    try:
        # Garantir que a nota é numérica
        df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

        media = df["nota"].mean()
        maior = df["nota"].max()
        menor = df["nota"].min()

        return {
            "media": round(media, 2),
            "maior": maior,
            "menor": menor
        }
    except Exception as e:
        return {
            "media": "Erro",
            "maior": "Erro",
            "menor": "Erro"
        }

def gerar_grafico(df, base_dir):
    # Garante que a nota é numérica
    df["nota"] = pd.to_numeric(df["nota"], errors="coerce")

    # Criar a figura
    plt.figure(figsize=(8, 4))

    # Gráfico de barras
    plt.bar(df["aluno"], df["nota"])
    plt.xlabel("Aluno")
    plt.ylabel("Nota")
    plt.title("Notas por Aluno")

    # Caminho da imagem
    caminho_img = os.path.join(base_dir, "static", "grafico_notas.png")

    # Salvar o arquivo
    plt.tight_layout()
    plt.savefig(caminho_img)
    plt.close()

    return "grafico_notas.png"