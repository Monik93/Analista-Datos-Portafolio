import pandas as pd
import requests
from datetime import datetime
import os

def extraer_api():
    print("Extrayendo API...")
    url = "https://fakestoreapi.com/products"
    data = requests.get(url).json()
    return pd.DataFrame(data)[['id','title','price','category']]

def transformar(df):
    df['fecha'] = datetime.now().strftime("%Y-%m-%d")
    df['alerta'] = df['price'].apply(lambda x: 'CARO' if x>100 else 'OK')
    return df

df = extraer_api()
df = transformar(df)
print(df.head())
print("Pipeline OK - listo para S3 y Power BI")
