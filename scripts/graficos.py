import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet('../data/silver/dados_tratados.parquet')

print("Dados carregados:", df.shape)

# ========================
# 1. Vendas por estado
# ========================
dados = df.groupby('customer_state')['price'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
dados.plot(kind='bar')

plt.title('Total de Vendas por Estado')
plt.xlabel('Estado')
plt.ylabel('Valor Total (R$)')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('../data/silver/graficos/vendas por estado.png')
plt.clf()

# ========================
# 2. Distribuição de preços
# ========================
plt.figure(figsize=(10,6))

df['price'].plot(kind='hist', bins=50)

plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.ylabel('Frequência')

plt.tight_layout()
plt.savefig('../data/silver/graficos/distr precos.png')
plt.clf()

# ========================
# 3. Vendas ao longo do tempo
# ========================
df.groupby(df['order_purchase_timestamp'].dt.to_period('M'))['price'].sum().plot()
plt.title('Vendas ao longo do tempo')
plt.savefig('../data/silver/graficos/vendas ao tempo.png')
plt.clf()
plt.xlabel('Mês')
plt.ylabel('Vendas')

# ========================
# 4. Top 10 cidades
# ========================
df['customer_city'].value_counts().head(10).plot(kind='bar')
plt.xticks(rotation=60)
plt.title('Top 10 cidades')
plt.savefig('../data/silver/graficos/top 10 cidades.png')
plt.clf()

# ========================
# 5. Frete médio por estado
# ========================
df.groupby('customer_state')['freight_value'].mean().plot(kind='bar')
plt.title('Frete médio por estado')
plt.savefig('../data/silver/graficos/frete medio por estado.png')
plt.clf()

print("Gráficos gerados!")