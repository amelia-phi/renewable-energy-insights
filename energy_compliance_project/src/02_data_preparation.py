import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the merged data
df=pd.read_csv('data/processed/demand_2021_2026.csv')

# 2. Convert SETTLEMENTDATE to datetime to allow for time-based operations
df['SETTLEMENTDATE'] = pd.to_datetime(df['SETTLEMENTDATE'])

# extract Time Features (To have more columns to compare)
df['Hour'] = df['SETTLEMENTDATE'].dt.hour
df['Month'] = df['SETTLEMENTDATE'].dt.month
df['DayOfWeek'] = df['SETTLEMENTDATE'].dt.dayofweek

# 3. Data cleaning
# check for missing values
null_counts = df.isna().sum()
print(null_counts)

# check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# 4. Descriptive Stat
print(df.describe())

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