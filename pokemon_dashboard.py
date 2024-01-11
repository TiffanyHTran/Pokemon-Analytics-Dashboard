import pandas as pd
from sqlalchemy import create_engine
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

#Extract and Transform Data
pokemon_data = pd.read_csv('pokemon.cvs')

