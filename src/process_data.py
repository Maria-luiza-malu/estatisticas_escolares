# src/process_data.py
import pandas as pd
import os

import pandas as pd
import os

def ler_arquivo(caminho):
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    if caminho.endswith(".csv"):
        df = pd.read_csv(caminho)
    elif caminho.endswith(".xlsx"):
        df = pd.read_excel(caminho, engine='openpyxl')  # <- aqui
    else:
        raise ValueError("Formato de arquivo não suportado. Use CSV ou XLSX")
    
    return df


def validar_dados(df):
    """
    Valida se o DataFrame contém colunas essenciais: 'Aluno' e 'Disciplina'
    """
    colunas_necessarias = ["Aluno", "Disciplina", "Nota"]
    for coluna in colunas_necessarias:
        if coluna not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {coluna}")
    
    # Substituir valores ausentes por 0
    df.fillna(0, inplace=True)
    return df