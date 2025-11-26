# src/process_data.py
import pandas as pd
import os

def ler_arquivo(caminho_arquivo):
    """
    Lê arquivo CSV ou Excel e retorna um DataFrame do pandas.
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
    
    extensao = os.path.splitext(caminho_arquivo)[1].lower()
    
    if extensao == ".csv":
        df = pd.read_csv(caminho_arquivo)
    elif extensao in [".xls", ".xlsx"]:
        df = pd.read_excel(caminho_arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado. Use CSV ou Excel.")
    
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