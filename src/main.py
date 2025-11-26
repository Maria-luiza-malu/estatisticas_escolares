# src/main.py
from process_data import ler_arquivo, validar_dados

def main():
    caminho = "data/notas_alunos.xlsx"  # arquivo de exemplo
    try:
        df = ler_arquivo(caminho)
        df = validar_dados(df)
        print("Arquivo lido com sucesso!")
        print(df.head())
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
