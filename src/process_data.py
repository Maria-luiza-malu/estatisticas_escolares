# src/process_data.py
import pandas as pd
import os

def ler_arquivo(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo, sep=",")
        return df
    except Exception as e:
        return f"Erro ao ler CSV: {str(e)}"


def validar_dados(df):
    if isinstance(df, str):
        return df  # já veio como erro

    colunas_esperadas = ["aluno", "matematica", "portugues", "ciencias"]
    for col in colunas_esperadas:
        if col not in df.columns:
            return f"Erro: coluna obrigatória ausente: {col}"

    return "Dados validados com sucesso!"