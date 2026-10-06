import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- Week 3: Pandas Tasks ---")

# 1. Read CSV file and verify structure
csv_path = 'Cars93_missing.csv'
try:
    df = pd.read_csv(csv_path, encoding='utf-8')
    print("1. CSV read successfully.")
    print(df.head())
    df.info()
except FileNotFoundError:
    print(f"Error: {csv_path} not found.")
    raise

# 2. Convert column to index
if 'Model' in df.columns:
    df['Model'] = df['Model'].astype(str)
    df.set_index('Model', inplace=True)
    print("\n2. 'Model' column set as index.")

# 3. Conditional data change
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').astype(float)
df.loc[df['Price'] < 10, 'Price'] = 10
print("\n3. Conditional update applied to 'Price'.")

# 4. Column names and missing values
column_names = df.columns.tolist()
missing_values_per_col = df.isna().sum()
total_lost_values = df.isna().sum().sum()

print("\n4. Column names:")
print(column_names)
print("\nMissing values per column:")
print(missing_values_per_col[missing_values_per_col > 0])
print(f"Total missing values: {total_lost_values}")

# 5. Swap two columns and sort columns alphabetically
def exchange_columns(data, col1, col2):
    if col1 in data.columns and col2 in data.columns:
        data[[col1, col2]] = data[[col2, col1]]
    return data

df = exchange_columns(df, 'Manufacturer', 'Type')
df = df.sort_index(axis=1)
print("\n5. Columns swapped and sorted:")
print(df.columns.tolist()[:6], "...")

# 6. Delete top and bottom 5%
q_low, q_high = df['Price'].quantile([0.05, 0.95])
initial_rows = len(df)
df = df[(df['Price'] >= q_low) & (df['Price'] <= q_high)]
print(f"\n6. Trimmed outliers. Rows: {initial_rows} -> {len(df)}")

# 7. Replace missing values with column average
price_mean = df['Price'].mean()
df['Price'] = df['Price'].fillna(price_mean)
print(f"\n7. Missing 'Price' filled with mean: {price_mean:.2f}")

# 8. Merge DataFrames and append column
dict1 = {'ID': [1, 2, 3], 'Value1': [10, 20, 30]}
dict2 = {'ID': [2, 3, 4], 'Value2': [40, 50, 60]}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

df_merged = pd.merge(df1, df2, on='ID', how='inner')
df1['NewColumn'] = df2['Value2']

print("\n8. Merged DataFrames:")
print(df_merged)
print("Appended column to df1:")
print(df1)

# 9. Histogram
plt.figure(figsize=(7, 4))
plt.hist(df['Price'].dropna(), bins=15, color='skyblue', edgecolor='black')
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)
plt.savefig('histogram.png')
plt.close()
print("\n9. Histogram saved as 'histogram.png'.")

# 10. Correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr(method='pearson')

print("\n10. Pearson Correlation Matrix:")
print(corr_matrix.iloc[:4, :4])
