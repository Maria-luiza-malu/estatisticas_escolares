# src/main.py
from process_data import ler_arquivo, validar_dados
from process_calculos import gerar_tabelas_resumo
def main():
    caminho = "data/notas_alunos.xlsx"  # arquivo de exemplo
    try:
        df = ler_arquivo(caminho)
        df = validar_dados(df)
        print("Arquivo lido com sucesso!")
        print(df.head())

        resumo = gerar_tabelas_resumo(df)
        print("\nMédias por aluno:")
        print(resumo["media_aluno"])
        print("\nMédias por disciplina:")
        print(resumo["media_disciplina"])
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
