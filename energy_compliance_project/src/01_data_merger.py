import pandas as pd
import glob
import os

# Define where the files are located
input_path = 'data/raw/'
output_path = 'data/processed/demand_2021_2026.csv'

# Get a list of all CSV files in the input folder
files = glob.glob('data/raw/*.csv')
print(f"Files found: {len(files)}")

if len(files) > 0:
    # Combine all files into a single DataFrame
    df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)    
    print(f"Merged Shape: {df.shape}")