# cars.json provided by jheer https://github.com/vega/vega/blob/main/docs/data/cars.json
import pandas as pd

# Cars DataFrame
car_df = pd.read_json('cars.json')
print(car_df)