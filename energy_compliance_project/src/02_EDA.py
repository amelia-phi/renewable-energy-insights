import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the merged data
df=pd.read_csv('data/processed/demand_processed_features.csv')

# Descriptive Stat
print(df.describe())

# set a style 
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = [12,6]

# --- PLOT 1: THE DUCK CURVE ---
plt.figure()
sns.lineplot(data=df, x='Hour', y='TOTALDEMAND', hue='REGION', errorbar=None)
plt.title('Average Demand Profile by Region: Identifying the Solar "Duck Curve"')
plt.ylabel('Demand (MW)')
plt.savefig('plots/duck_curve.png')

# --- PLOT 2: PRICE VOLATILITY ---
plt.figure()
# We filter RRP between -200 and 500 just to see the main distribution clearly
sns.boxplot(data=df, x='Hour', y='RRP', showfliers=False) 
plt.title('Hourly Price Distribution: Identifying Market Instability Windows')
plt.savefig('plots/price_volatility.png')

# --- PLOT 3: SEASONAL IMPACT ---
# Create a pivot table for the heatmap
pivot = df.groupby(['Hour', 'Month'])['Is_Negative_Price'].mean().unstack()
plt.figure(figsize=(10, 8))
sns.heatmap(pivot, cmap='YlOrRd', annot=False)
plt.title('Heatmap of Negative Price Frequency (Solar Over-saturation Risk)')
plt.savefig('plots/risk_heatmap.png')

print("EDA Plots generated successfully in the /plots folder!")