# cars.csv provided by noamross https://gist.github.com/noamross/e5d3e859aa0c794be10b#file-cars-csv

import pandas as pd

# Cars DataFrame
car_df = pd.read_csv('cars.csv')

# Print First 10 Rows
print(car_df.head(10))

# Print Last 10 Rows
print(car_df.tail(10))

# DataFrame Information
print(car_df.info())

