import sqlite3
import pandas as pd

# load data
df = pd.read_csv('data/processed/demand_2021_2026.csv')

# establish sql env
# connect to db
conn = sqlite3.connect('energy_analytic.db')

# push cleaned df to sql
df.to_sql('fact_energy', conn, if_exists='replace', index=False)

