import pandas as pd
from sqlalchemy import create_engine
import os

print("INÍCIO GOLD")

# ========================
# 1. LEITURA
# ========================
print("Carregando dados tratados")

df = pd.read_parquet('../data/silver/dados_tratados.parquet')

print("Dados carregados:", df.shape)

# ========================
# 2. DIMENSÃO CLIENTE
# ========================
print("Criando dim_cliente")

dim_cliente = df[['customer_id', 'customer_city', 'customer_state']].drop_duplicates()

print("Dim Cliente:", dim_cliente.shape)

# ========================
# 3. DIMENSÃO DATA
# ========================
print("Criando dim_data")

dim_data = pd.DataFrame()
dim_data['data'] = pd.to_datetime(df['order_purchase_timestamp']).dt.date

print("Antes:", dim_data.shape)

dim_data = dim_data.drop_duplicates()
dim_data['mes'] = pd.to_datetime(dim_data['data']).dt.month
dim_data['ano'] = pd.to_datetime(dim_data['data']).dt.year

print("Depois:", dim_data.shape)

# ========================
# 4. FATO VENDAS
# ========================
print("Criando fato_vendas")

fato_vendas = df[[
    'order_id',
    'customer_id',
    'price',
    'freight_value',
    'order_purchase_timestamp'
]]

print("Fato Vendas:", fato_vendas.shape)

# ========================
# 5. CONEXÃO
# ========================
print("Conectando ao banco")

engine = create_engine('postgresql://postgres:Armaria26!@localhost:5432/projeto_dados')

# ========================
# 6. ENVIO
# ========================
print("Enviando tabelas")

dim_cliente.to_sql('dim_cliente', engine, if_exists='replace', index=False)
dim_data.to_sql('dim_data', engine, if_exists='replace', index=False)

fato_vendas.to_sql(
    'fato_vendas',
    engine,
    if_exists='replace',
    index=False,
    chunksize=10000
)

print("GOLD FINALIZADO COM SUCESSO!")

print("FIM GOLD")