# Biblioteca
import pymongo
import os
import pandas as pd
import json

# Conexão com o MongoDB
# Cria conexão local
client = pymongo.MongoClient('mongodb://localhost:27017')
print(client)

# Carregando o dataset
# Import dataframe
whrdataset = pd.read_csv('https://raw.githubusercontent.com/digonfernan/mongodb-test/main/world-happiness-report-2021.csv')

# Visualiza os dados
whrdataset.shape
whrdataset.head()

# Preparando para o export
# Cria um dicionário
whrdic = whrdataset.to_dict(orient = 'records')
# Visualiza o dicionário
whrdic

# Exportando para o MongoDB
# Cria o database
whrdb = client['whrtotal']
# Visualiza o database
print(whrdb)

# Export o database
whrdb.whrdb21.insert_many(whrdic)