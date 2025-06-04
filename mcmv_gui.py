import matplotlib
matplotlib.use("TkAgg")

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

def simular():
    try:
        renda = float(entry_renda.get())
        valor_imovel = float(entry_valor.get())
        fgts = float(entry_fgts.get())

        # Determinar subsídio estimado com base na renda
        if renda <= 6000:
            subsidio = 20000
        elif renda <= 7000:
            subsidio = 10000
        else:
            subsidio = 0

        financiamento = valor_imovel * 0.80
        entrada_necessaria = valor_imovel - financiamento - subsidio - fgts
        entrada_necessaria = max(entrada_necessaria, 0)

        dados = {
            "Renda Familiar (R$)": [renda],
            "Valor do Imóvel (R$)": [valor_imovel],
            "Financiamento (80%) (R$)": [financiamento],
            "Subsídio Estimado (R$)": [subsidio],
            "FGTS (R$)": [fgts],
            "Entrada a Pagar (R$)": [entrada_necessaria]
        }

        df = pd.DataFrame(dados)
        df.to_excel("simulacao_mcmv_gui.xlsx", index=False)

        # Gráfico
        fig, ax = plt.subplots(figsize=(8, 5))
        labels = [f"Renda: R${renda:,.0f}"]
        entrada = df["Entrada a Pagar (R$)"]
        fgts_val = df["FGTS (R$)"]
        subsidio_val = df["Subsídio Estimado (R$)"]

        ax.bar(labels, entrada, label='Entrada a Pagar (R$)', color='red')
        ax.bar(labels, fgts_val, bottom=entrada, label='FGTS (R$)', color='orange')
        ax.bar(labels, subsidio_val, bottom=entrada + fgts_val, label='Subsídio (R$)', color='green')

        ax.set_ylabel('Valores (R$)')
        ax.set_title('Composição da Entrada no MCMV')
        ax.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Interface gráfica
root = tk.Tk()
root.title("Simulador MCMV - Caixa Econômica")

tk.Label(root, text="Renda Familiar (R$):").grid(row=0, column=0, sticky="e")
entry_renda = tk.Entry(root)
entry_renda.grid(row=0, column=1)

tk.Label(root, text="Valor do Imóvel (R$):").grid(row=1, column=0, sticky="e")
entry_valor = tk.Entry(root)
entry_valor.grid(row=1, column=1)

tk.Label(root, text="FGTS Disponível (R$):").grid(row=2, column=0, sticky="e")
entry_fgts = tk.Entry(root)
entry_fgts.grid(row=2, column=1)

btn = tk.Button(root, text="Simular", command=simular)
btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
