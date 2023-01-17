# cars.csv provided by noamross https://gist.github.com/noamross/e5d3e859aa0c794be10b#file-cars-csv
import pandas as pd

# Cars DataFrame
car_df = pd.read_csv('cars.csv')
print(car_df)

# Check Maximum Number Of Displayed Rows
print(pd.options.display.max_rows)