import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the merged data
df=pd.read_csv('data/processed/demand_2021_2026.csv')

# Descriptive Stat
print(df.describe())

# identify "solar saturation (negative pricing)"
# Negative prices in the NEM are a strong proxy for solar over-supply
df['Negative_Price_Flag'] = df['RRP'] < 0

# scatterplot matrix on selected columns
# including Hour and Month allows you to see seasonal/daily cycles
cols_to_compare = ['TOTALDEMAND', 'RRP', 'Hour', 'Month']
# sample 2000 points for easy visualisation
sns.set_theme(style="ticks")

g = sns.pairplot(
    df.sample(n=min(len(df), 20000)), 
    vars=cols_to_compare, 
    hue='REGION', 
    palette='husl',
    plot_kws={'alpha': 0.5, 's': 10} # 's' is dot size, 'alpha' is transparency
)

g.fig.suptitle("Comprehensive Scatterplot Matrix: Demand, Price, and Time", y=1.02)
plt.savefig('energy_matrix.png')
plt.show()

