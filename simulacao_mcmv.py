import pandas as pd
import matplotlib.pyplot as plt

# Dados dos cenários
cenarios = [
    {
        "Renda Familiar (R$)": 5500,
        "Valor do Imóvel (R$)": 360000,
        "Financiamento (80%) (R$)": 288000,
        "Subsídio Estimado (R$)": 20000,
        "FGTS (R$)": 18000
    },
    {
        "Renda Familiar (R$)": 8200,
        "Valor do Imóvel (R$)": 360000,
        "Financiamento (80%) (R$)": 288000,
        "Subsídio Estimado (R$)": 0,
        "FGTS (R$)": 18000
    }
]

# Cálculo da entrada necessária
for c in cenarios:
    valor_imovel = c["Valor do Imóvel (R$)"]
    financiamento = c["Financiamento (80%) (R$)"]
    subsidio = c["Subsídio Estimado (R$)"]
    fgts = c["FGTS (R$)"]
    entrada_necessaria = valor_imovel - financiamento - subsidio - fgts
    c["Entrada a Pagar (R$)"] = max(entrada_necessaria, 0)

# Criar DataFrame
df = pd.DataFrame(cenarios)

# Salvar em Excel para edição
df.to_excel("simulacao_mcmv.xlsx", index=False)

# Criar gráfico
fig, ax = plt.subplots(figsize=(10, 6))
labels = ["Renda: R$5.500", "Renda: R$8.200"]
entrada = df["Entrada a Pagar (R$)"]
subsidiado = df["Subsídio Estimado (R$)"]
fgts = df["FGTS (R$)"]

# Barras empilhadas
ax.bar(labels, entrada, label='Entrada a Pagar (R$)', color='red')
ax.bar(labels, fgts, bottom=entrada, label='FGTS (R$)', color='orange')
ax.bar(labels, subsidiado, bottom=entrada+fgts, label='Subsídio (R$)', color='green')

ax.set_ylabel('Valores (R$)')
ax.set_title('Composição da Entrada no MCMV - Simulação Caixa')
ax.legend()
plt.tight_layout()

plt.show()
