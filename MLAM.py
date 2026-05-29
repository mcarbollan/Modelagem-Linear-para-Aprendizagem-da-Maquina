# ==========================================
# GLOBAL SOLUTION 2026.1
# MODELAGEM LINEAR PARA APRENDIZAGEM DE MÁQUINA
# ==========================================

# IMPORTAÇÃO DAS BIBLIOTECAS

import pandas as pd
import matplotlib.pyplot as plt
import statistics

# ==========================================
# LEITURA DA BASE DE DADOS
# ==========================================

# Exemplo:
# Substitua "dados.csv" pelo nome da sua base

dados = pd.read_csv("dados.csv")

# Mostrar primeiras linhas
print("BASE DE DADOS")
print(dados.head())

# INFORMAÇÕES GERAIS

print("INFORMAÇÕES DA BASE")
print(dados.info())

# TABELA DE FREQUÊNCIA
# VARIÁVEL DISCRETA

# Exemplo usando uma coluna discreta

frequencia_discreta = dados["Quantidade"].value_counts()

print("TABELA DE FREQUÊNCIA - DISCRETA")
print(frequencia_discreta)

# TABELA DE FREQUÊNCIA
# VARIÁVEL CONTÍNUA

# Exemplo usando uma coluna contínua

frequencia_continua = pd.cut(
    dados["Valor"],
    bins=5
).value_counts()

print("\n===== TABELA DE FREQUÊNCIA - CONTÍNUA =====")
print(frequencia_continua)

# GRÁFICO 1 - BARRAS

plt.figure(figsize=(8, 5))

dados["Categoria"].value_counts().plot(
    kind="bar",
    color="skyblue"
)

plt.title("Distribuição por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade")

plt.show()

# GRÁFICO 2 - HISTOGRAMA

plt.figure(figsize=(8, 5))

plt.hist(
    dados["Valor"],
    bins=10,
    color="orange",
    edgecolor="black"
)

plt.title("Distribuição dos Valores")
plt.xlabel("Valores")
plt.ylabel("Frequência")

plt.show()

# ==========================================
# ANÁLISE ESTATÍSTICA
# ==========================================

valores = dados["Valor"]

# Média
media = valores.mean()

# Mediana
mediana = valores.median()

# Moda
moda = statistics.mode(valores)

# Máximo
maximo = valores.max()

# Mínimo
minimo = valores.min()

# Amplitude
amplitude = maximo - minimo

# Variância
variancia = valores.var()

# Desvio padrão
desvio_padrao = valores.std()

# Quartis
quartis = valores.quantile([0.25, 0.50, 0.75])

# ==========================================
# RESULTADOS
# ==========================================

print("ANÁLISE ESTATÍSTICA")

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

print(f"\nValor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")
print(f"Amplitude: {amplitude}")

print(f"\nVariância: {variancia}")
print(f"Desvio padrão: {desvio_padrao}")

print("\nQuartis:")
print(quartis)

# ==========================================
# INTERPRETAÇÃO DOS RESULTADOS
# ==========================================

print("INTERPRETAÇÃO")

print(
    "A média representa o valor médio dos dados analisados."
)

print(
    "A mediana mostra o valor central da distribuição."
)

print(
    "O desvio padrão indica o nível de dispersão dos dados."
)

print(
    "Os quartis ajudam a entender a distribuição dos valores."
)

# ==========================================
# RELATÓRIO FINAL
# ==========================================

print("RELATÓRIO FINAL")

print(
    "A análise estatística permitiu identificar padrões "
    "importantes na base de dados."
)

print(
    "Os gráficos facilitaram a visualização das distribuições "
    "e tendências dos dados."
)

print(
    "As medidas estatísticas ajudaram na interpretação "
    "do comportamento das variáveis analisadas."
)