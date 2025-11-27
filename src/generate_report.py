# src/generate_report.py
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import os

def gerar_graficos(df, caminho_saida):
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)

    for aluno in df["Aluno"].unique():
        dados_aluno = df[df["Aluno"] == aluno]
        plt.figure(figsize=(6,4))
        plt.bar(dados_aluno["Disciplina"], dados_aluno["Nota"])
        plt.title(f"Desempenho de {aluno}")
        plt.ylabel("Nota")
        plt.xlabel("Disciplina")

        arquivo_grafico = os.path.join(caminho_saida, f"{aluno}_grafico.png")
        plt.savefig(arquivo_grafico)
        plt.close()

def gerar_pdf_boletim(df, caminho_saida):
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)

    for aluno in df["Aluno"].unique():
        dados_aluno = df[df["Aluno"] == aluno]
        arquivo_pdf = os.path.join(caminho_saida, f"{aluno}_boletim.pdf")
        c = canvas.Canvas(arquivo_pdf)
        c.setFont("Helvetica", 12)

        c.drawString(100, 800, f"Boletim de {aluno}")
        y = 750

        for idx, row in dados_aluno.iterrows():
            c.drawString(100, y, f"{row['Disciplina']}: {row['Nota']}")
            y -= 25

        c.save()
