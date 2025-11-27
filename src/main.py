# src/main.py
from process_data import ler_arquivo, validar_dados
from process_calculos import gerar_tabelas_resumo
from generate_report import gerar_pdf_boletim, gerar_graficos
import os


def main():
    caminho = "data/notas_alunos.xlsx"
    caminho_saida = "output/"

    try:
        df = ler_arquivo(caminho)
        df = validar_dados(df)
        print("Arquivo lido com sucesso!")

        resumo = gerar_tabelas_resumo(df)
        print(resumo["media_aluno"])
        print(resumo["media_disciplina"])

        # Geração de gráficos e PDFs
        gerar_graficos(df, caminho_saida)
        gerar_pdf_boletim(df, caminho_saida)

        print(f"Boletins e gráficos salvos em '{caminho_saida}'")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()