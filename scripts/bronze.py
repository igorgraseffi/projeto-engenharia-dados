import pandas as pd

caminho = '../data/raw/olist_order_items_dataset.csv'

df = pd.read_csv(caminho)

print(df.head())
print(df.shape)