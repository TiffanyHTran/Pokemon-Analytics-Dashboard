import pandas as pd
from sqlalchemy import create_engine

# Extract data from pokemon.csv
pokemon_data = pd.read_csv('pokemon.cvs')

# Transform data and create dimension tables
dim_pokemon = pokemon_data[['ID', 'Name', 'Type1', 'Type2', 'Generation']].copy()

# Concatenate Type1 and Type2, then get unique values
unique_types = pd.concat([pokemon_data['Type1'], pokemon_data['Type2']]).unique()
dim_type = pd.DataFrame({'type_name': unique_types})

dim_stat = pd.DataFrame({'stat_name': ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']})
dim_stat_value = pd.DataFrame({'value': pokemon_data[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].stack().unique()})

# Load dimension tables into the data warehouse
engine = create_engine('sqlite:///pokemon_data_warehouse_complex.db')
dim_pokemon.to_sql('dim_pokemon', engine, if_exists='replace', index=False)
dim_type.to_sql('dim_type', engine, if_exists='replace', index=False)
dim_stat.to_sql('dim_stat', engine, if_exists='replace', index=False)
dim_stat_value.to_sql('dim_stat_value', engine, if_exists='replace', index=False)

# Transform data and create fact table
fact_pokemon_stat = pd.melt(pokemon_data, id_vars=['ID'], value_vars=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'],
                            var_name='stat_name', value_name='value')
fact_pokemon_stat = pd.merge(fact_pokemon_stat, dim_pokemon, left_on='ID', right_on='ID')
fact_pokemon_stat = pd.merge(fact_pokemon_stat, dim_type, left_on='Type1', right_on='type_name', how='left')
fact_pokemon_stat = pd.merge(fact_pokemon_stat, dim_stat, left_on='stat_name', right_on='stat_name')
fact_pokemon_stat = pd.merge(fact_pokemon_stat, dim_stat_value, left_on='value', right_on='value')

# Load the fact table into the data warehouse
fact_pokemon_stat.to_sql('fact_pokemon_stat', engine, if_exists='replace', index=False)

print("Data Warehousing Completed")
