# data.csv provided by W3Schools https://www.w3schools.com/python/pandas/data.csv
import pandas as pd

# Remove Rows with null cells
data_df = pd.read_csv('data.csv')
cleaned_df = data_df.dropna()
print(cleaned_df)

# Remove Rows with null cells inplace
# data_df.dropna(inplace = True)
# print(data_df)

# Replace null values with set number
# data_df.fillna(130, inplace = True)

# Replace null values in specific colimn
# df["Calories"].fillna(130, inplace = True)

