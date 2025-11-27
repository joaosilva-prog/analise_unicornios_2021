"""Projeto Startups Unicórnios 2021

"Unicórnios" no setor de startups são empresas privadas que atingem uma avaliação de mercado de US$ 1 bilhão ou mais. O termo foi cunhado pela investidora Aileen Lee em 2013 para descrever a raridade dessas empresas, que se destacam por seu rápido crescimento e capacidade de inovar de forma disruptiva.
Em cima disso, vamos gerar análises em cima de uma base de dados desse tipo de startups do ano de 2021.

# Imports
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

"""# Leitura dos Dados"""

dados_raw = pd.read_csv("Startups+in+2021+end.csv")

dados_raw.shape

"""# Inspeções Iniciais"""

dados_raw.head()

dados_raw.columns

"""# Renomeando Colunas"""

dados_raw.rename(columns = {
    'Unnamed: 0' : 'Id',
    'Company' : 'Empresa',
    'Valuation ($B)' : 'Valor ($)',
    'Date Joined' : 'Data de Adesão',
    'Country' : 'Pais',
    'City' : 'Cidade',
    'Industry': 'Setor',
    'Select Investors': 'Investidores',
}, inplace=True )

dados_raw.head()

dados_raw.info()

"""# Verificação de Nulos"""

dados_raw.isnull().sum()

plt.figure(figsize=(15,6))
plt.title("Campos Nulos")
sns.heatmap(dados_raw.isnull(), cmap = "viridis", cbar = False);

"""# Análise de Campos Únicos"""

dados_raw.nunique()

dados_raw["Setor"].unique()

dados_raw["Setor"].value_counts()

round(dados_raw["Setor"].value_counts(normalize = True) * 100, 2)

plt.figure(figsize=(15,6))
plt.title("Setores")
plt.bar(dados_raw["Setor"].value_counts().index, dados_raw["Setor"].value_counts())
plt.xticks(rotation = 45, ha = "right");

"""# Análise de Distribuição de Países"""

paises = round(dados_raw["Pais"].value_counts() * 100, 2)

plt.figure(figsize=(9,6))
plt.title("Distribuição de Países - Top 10", pad = 40)
plt.pie(
    paises.head(10),
    startangle = 90,
    autopct = "%1.1f%%",
    pctdistance = 1.1,
    explode = (0.02,
               0.03,
               0.04,
               0.05,
               0.06,
               0.07,
               0.08,
               0.11,
               0.14,
               0.18
    )
)
plt.legend(paises.index[0:10], loc = "center right", bbox_to_anchor=(1, 0, 0.5, 1));

"""# Análise de Startups por Ano e País"""

dados_raw["Data de Adesão"] = pd.to_datetime(dados_raw["Data de Adesão"])

dados_raw["Data de Adesão"].head()

dados_raw["Mês"] = pd.DatetimeIndex(dados_raw["Data de Adesão"]).month
dados_raw["Ano"] = pd.DatetimeIndex(dados_raw["Data de Adesão"]).year

dados_raw.head()

analise_agrupada = dados_raw.groupby(["Pais", "Ano", "Mês", "Empresa"]).count()["Id"].reset_index()

analise_agrupada

analise_agrupada.loc[
    analise_agrupada["Pais"] == "Brazil"
]

dados_raw["Valor ($)"] = pd.to_numeric(dados_raw["Valor ($)"].apply(lambda linha: linha.replace("$", "")))

dados_raw.head()

analise_pais = dados_raw.groupby(["Pais"])["Valor ($)"].sum().reset_index().sort_values("Valor ($)", ascending = False)

analise_pais.head()

plt.figure(figsize=(16,6))
plt.title("Análise de Valor por País")
plt.plot(analise_pais["Pais"], analise_pais["Valor ($)"]);
plt.xticks(rotation = 45, ha = "right");