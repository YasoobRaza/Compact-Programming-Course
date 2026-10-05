import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Pandas Tasks")

# 1. Read CSV file and transfer it into DataFrame
df = pd.read_csv('Cars93_missing.csv')
print("\nTask 1: DataFrame loaded")

# 2. Transfer object Series into index column of the dataframe
if 'Model' in df.columns:
    df.set_index('Model', inplace=True)
print("Task 2: Index set to Model")

# 3. Change the data in the column of DataFrame according to some condition
# Condition: if Price < 10, set to 10
if 'Price' in df.columns:
    df.loc[df['Price'] < 10, 'Price'] = 10
print("Task 3: Price updated")

# 4. Get names of the DataFrame columns and sum of losted values DF
columns = df.columns
lost_values = df.isnull().sum().sum()
print("\nTask 4:")
print("Columns:", list(columns))
print("Sum of lost values:", lost_values)

# 5. Ex-change 2 columns, use function for it. Sort coulumn by name
def exchange_columns(dataframe, col1, col2):
    if col1 not in dataframe.columns or col2 not in dataframe.columns:
        return dataframe
    cols = list(dataframe.columns)
    idx1 = cols.index(col1)
    idx2 = cols.index(col2)
    cols[idx1], cols[idx2] = cols[idx2], cols[idx1]
    return dataframe[cols]

df = exchange_columns(df, 'Manufacturer', 'Type')
df = df.reindex(sorted(df.columns), axis=1)
print("\nTask 5: Columns exchanged and sorted")

# 6. Delete upper and lower 5% in object DataFrame
if 'Price' in df.columns:
    q_low = df['Price'].quantile(0.05)
    q_high = df['Price'].quantile(0.95)
    df = df[(df['Price'] >= q_low) & (df['Price'] <= q_high)]
print("Task 6: 5% upper and lower deleted")

# 7. Replay (Apply) missed values in the Column with average values.
if 'Price' in df.columns:
    mean_price = df['Price'].mean()
    df['Price'] = df['Price'].fillna(mean_price)
print("Task 7: Missed values in Price replaced with average")

# 8. Create two data frames using the two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
dict1 = {'ID': [1, 2, 3], 'Value1': [10, 20, 30]}
dict2 = {'ID': [2, 3, 4], 'Value2': [40, 50, 60]}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

df_merged = pd.merge(df1, df2, on='ID', how='inner')
df1['NewColumn'] = pd.Series([100, 200, 300]) # append a new column
print("\nTask 8: DataFrames merged")
print(df_merged)

# 9. For any column create histogram
if 'Price' in df.columns:
    df['Price'].hist()
    plt.title("Price Histogram")
    plt.savefig('histogram.png')
    print("\nTask 9: Histogram saved")

# 10. Create Correlation Matrix for any column
df_numeric = df.select_dtypes(include=[np.number])
corr_matrix = df_numeric.corr()
print("\nTask 10: Correlation matrix")
print(corr_matrix)
