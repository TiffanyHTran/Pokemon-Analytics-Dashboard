import pandas as pd
from sqlalchemy import create_engine

#Extract data from pokemon.cvs
pokemon_data = pd.read_csv('pokemon.cvs')

#Tranform data and create dimension tables
dim_pokemon = pokemon_data[['ID', 'Name', 'Type1', 'Type2', 'Generation']].copy()
dim_type = pd.DataFrame({'type_name': pokemon_data['Type1'].append(pokemon_data['Type2']).unique()})
dim_stat = pd.DataFrame({'stat_name': ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']})
dim_stat_value = pd.DataFrame({'value': pokemon_data[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].stack().unique()})

#Load dimension tables into the data warehouse
engine = create_engine('sqlite:///pokemon_data_warehouse_complex.db')
dim_pokemon.to_sql('dim_pokemon', engine, if_exists='replace', index=False)
dim_type.to_sql('dim_type', engine, if_exists='replace', index=False)
dim_stat.to_sql('dim_stat', engine, if_exists='replace', index=False)
dim_stat_value.to_sql('dim_stat_value', engine, if_exists='replace', index=False)

