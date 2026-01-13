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

# --- THE DUCK CURVE ---
plt.figure()
sns.lineplot(data=df, x='Hour', y='TOTALDEMAND', hue='REGION', errorbar=None)
plt.title('Average Demand Profile by Region: Identifying the Solar "Duck Curve"')
plt.ylabel('Demand (MW)')
plt.xticks(range(0, 24, 2))
plt.savefig('plots/duck_curve.png')

# --- PRICE VOLATILITY ---
plt.figure()
# We filter RRP between -200 and 500 just to see the main distribution clearly
sns.boxplot(data=df, x='Hour', y='RRP', showfliers=False, hue="REGION") 
plt.title('Hourly Price Distribution: Identifying Market Instability Windows')
plt.savefig('plots/price_volatility.png')

# --- SEASONAL IMPACT ---
# Create a pivot table for the heatmap
pivot = df.groupby(['Hour', 'Month'])['Is_Negative_Price'].mean().unstack()
plt.figure(figsize=(10, 8))
sns.heatmap(pivot, cmap='YlOrRd', annot=False)
plt.title('Heatmap of Negative Price Frequency (Solar Over-saturation Risk)')
plt.savefig('plots/risk_heatmap.png')

# --- Seasonal Demand Curves ---
plt.figure(figsize=(12, 6))
# Define seasons for clearer labeling
month_to_season = {12:'Summer', 1:'Summer', 2:'Summer', 3:'Autumn', 4:'Autumn', 5:'Autumn', 
                  6:'Winter', 7:'Winter', 8:'Winter', 9:'Spring', 10:'Spring', 11:'Spring'}
df['Season'] = df['Month'].map(month_to_season)

sns.lineplot(data=df, x='Hour', y='TOTALDEMAND', hue='Season', errorbar=None)
plt.title('Seasonal Demand Profiles: Impact of Weather on the Duck Curve')
plt.ylabel('Demand (MW)')
plt.savefig('plots/seasonal_demand_profiles.png')

# --- Correlation Heatmap ---
plt.figure(figsize=(10, 8))
corr = df[['TOTALDEMAND', 'RRP', 'Hour', 'Month', 'DayOfWeek', 'Is_Negative_Price']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Feature Correlation Matrix: Identifying Drivers of Grid Stress')
plt.savefig('plots/correlation_heatmap.png')

# --- Weekday vs Weekend Profile ---
df['Is_Weekend'] = df['DayOfWeek'].isin([5, 6])
plt.figure()
sns.lineplot(data=df, x='Hour', y='TOTALDEMAND', hue='Is_Weekend', errorbar=None)
plt.title('Demand Profiles: Weekday vs. Weekend (Solar Penetration Impact)')
plt.savefig('plots/weekday_weekend_comparison.png')

# --- Monthly Negative Price Frequency ---
plt.figure(figsize=(10, 6))
seasonal_risk = df.groupby('Month')['Is_Negative_Price'].mean() * 100
seasonal_risk.plot(kind='bar', color='salmon')
plt.title('Percentage of Negative Price Intervals by Month (Compliance Risk)')
plt.ylabel('% Frequency')
plt.xticks(rotation=0)
plt.savefig('plots/monthly_risk_bar.png')
