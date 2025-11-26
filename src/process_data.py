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

