import pandas as pd

def calcular_media_aluno(df):
    """
    Calcula a média de cada aluno.
    """
    media_aluno = df.groupby("Aluno")["Nota"].mean().reset_index()
    media_aluno.rename(columns={"Nota": "Media_Aluno"}, inplace=True)
    return media_aluno

def calcular_media_disciplina(df):
    """
    Calcula a média de cada disciplina.
    """
    media_disciplina = df.groupby("Disciplina")["Nota"].mean().reset_index()
    media_disciplina.rename(columns={"Nota": "Media_Disciplina"}, inplace=True)
    return media_disciplina

def gerar_tabelas_resumo(df):
    """
    Retorna dicionário com tabelas resumo por aluno e por disciplina
    """
    resumo = {
        "media_aluno": calcular_media_aluno(df),
        "media_disciplina": calcular_media_disciplina(df)
    }
    return resumo