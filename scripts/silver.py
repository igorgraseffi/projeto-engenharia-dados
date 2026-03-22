print("INÍCIO DO PROCESSO")
import pandas as pd

print("Lendo arquivos...")
orders_path = '../data/raw/olist_orders_dataset.csv'
items_path = '../data/raw/olist_order_items_dataset.csv'
customers_path = '../data/raw/olist_customers_dataset.csv'
geo_path = '../data/raw/olist_geolocation_dataset.csv'

geo = pd.read_csv(geo_path)
orders = pd.read_csv(orders_path)
items = pd.read_csv(items_path)
customers = pd.read_csv(customers_path)

print("Orders:", orders.shape)
print("Items:", items.shape)
print("Customers:", customers.shape)
print("Geo:", geo.shape)

print("INÍCIO DOS JOINS")

print("Join 1: orders + items")
df = pd.merge(orders, items, on='order_id', how='inner')

print("Join 2: + customers")
df = pd.merge(df, customers, on='customer_id', how='inner')

print("Resultado:", df.shape)
print(df.head())

print("join 3: + geolocation")
df = pd.merge(
    df,
    geo,
    left_on='customer_zip_code_prefix',
    right_on='geolocation_zip_code_prefix',
    how='left'
)

print("Resultado:", df.shape)

print("FIM DOS JOINS")

print("Verificando nulos")
print(df.isnull().sum())

print("Tipos de dados")
print(df.dtypes)

print("INÍCIO DA LIMPEZA")
df.columns = df.columns.str.lower()
df = df.drop_duplicates()

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_approved_at'] = df['order_approved_at'].fillna('Não aprovado')

print("Após limpeza:", df.shape)

print("FIM DA LIMPEZA")

df.columns = df.columns.str.lower()
df.to_parquet('../data/silver/dados_tratados.parquet')

print("Dados salvos na camada Silver")

import os

os.makedirs('../data/silver', exist_ok=True)
