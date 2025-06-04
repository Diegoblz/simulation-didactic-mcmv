# simulation-didactic-mcmv

# 🏠 Simulador Minha Casa 

Este é um simulador gráfico simples que estima a composição da **entrada de um financiamento habitacional via o programa Minha Casa Minha Vida (MCMV)** da **Caixa Econômica Federal**.

Você informa:
- ✅ Renda familiar
- ✅ Valor do imóvel
- ✅ FGTS disponível

E recebe como resultado:
- 💰 Estimativa da entrada a pagar
- 📉 Gráfico com a composição dos valores
- 📊 Planilha Excel gerada automaticamente

---

## 📋 Requisitos

### Linux Mint / Ubuntu / Debian

1. **Python 3 instalado** (geralmente já vem com o sistema):
   ```bash
   python3 --version

2. **Instalar dependências**:

```bash
sudo apt update
sudo apt install python3-pip python3-tk tk-dev -y
pip3 install pandas matplotlib openpyxl pillow
```

### Windows

1. Instale o **Python 3**:
   - Acesse: https://www.python.org/downloads/windows/
   - Baixe o instalador do Python 3
   - Marque a opção **"Add Python to PATH"** na instalação
2. Abra o **Prompt de Comando (cmd)** e instale os pacotes:

```bash
pip install pandas matplotlib openpyxl pillow
```

## ▶️ Como executar

1. Baixe ou crie o arquivo `mcmv_gui.py` com o seguinte conteúdo:

   (→ Ver abaixo na seção **Código Fonte** 👇)

2. No terminal (Linux) ou Prompt de Comando (Windows), vá até a pasta do arquivo:

   ```
   bash
   
   
   CopiarEditar
   cd caminho/para/o/arquivo
   ```

3. Execute com:

   ```bash
   python3 mcmv_gui.py   # Linux
   ```

   ou

   ```bash
   python mcmv_gui.py    # Windows
   ```

##  Saída

- Será exibido um **gráfico de barras empilhadas** com os valores de entrada.
- Será criado um arquivo chamado `simulacao_mcmv_gui.xlsx` com os dados da simulação.
