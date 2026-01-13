import pandas as pd
import glob
import os

# 1. SETUP PATHS
input_path = 'data/raw/'
merge_output = 'data/processed/demand_2021_2026.csv'
feature_output = 'data/processed/demand_processed_features.csv'

# 2. MERGE RAW FILES 
files = glob.glob(os.path.join(input_path, '*.csv'))
print(f"Files found: {len(files)}")

if not files:
    print("No files found in data/raw/!")
else:
    # Combine all files exactly as they are
    df_raw = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
    
    # Save the merged raw file first
    os.makedirs('data/processed', exist_ok=True)
    df_raw.to_csv(merge_output, index=False)
    print(f"1. Merged raw data saved to: {merge_output}")

    # 3. FEATURE ENGINEERING (Silver Layer)
    # Work on a copy to keep df_raw pristine
    df = df_raw.copy()

    # Convert date and sort
    df['SETTLEMENTDATE'] = pd.to_datetime(df['SETTLEMENTDATE'])
    df = df.sort_values(by=['REGION', 'SETTLEMENTDATE'])

    # Extract Time Features
    df['Hour'] = df['SETTLEMENTDATE'].dt.hour
    df['Month'] = df['SETTLEMENTDATE'].dt.month
    df['DayOfWeek'] = df['SETTLEMENTDATE'].dt.dayofweek
    
    # Add your solar-proxy indicator
    df['Is_Negative_Price'] = (df['RRP'] < 0).astype(int)

    # 4. CLEANING
    df = df.ffill().drop_duplicates()

    # 5. SAVE THE PROCESSED FEATURES
    df.to_csv(feature_output, index=False)
    print(f"2. Processed features saved to: {feature_output}")

print("\n--- FINAL VERIFICATION ---")
print(f"New Columns added: {[col for col in df.columns if col not in df_raw.columns]}")