import pandas as pd
from sqlalchemy import create_engine

#Extract data from pokemon.cvs
pokemon_data = pd.read_csv('pokemon.cvs')


#Transform data by creating a new column 'Overall'
#'Overall' value is the sum of the value colums HP, Attack, Defense, Sp.Attk, Sp.Def, and Speed
#These attributes are indicative of a Pokemon's health, offense, defense, and speed capabilities in battle
pokemon_data['Overall'] = pokemon_data[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].sum(axis=1)

#Load transformed data into a SQLite database
engine = create_engine('sqlite:///pokemon_database.db')
pokemon_data.to_sql('pokemon', engine, if_exists='replace', index=False)

print("ETL Pipeline Completed")
