import pandas as pd

# 1. Load the merged data
df=pd.read_csv('data/processed/demand_2021_2026.csv')

print("--- COLUMN DATATYPES ---")
print(df.dtypes)

# 2. Convert SETTLEMENTDATE to datetime to allow for time-based operations
df['SETTLEMENTDATE'] = pd.to_datetime(df['SETTLEMENTDATE'])

