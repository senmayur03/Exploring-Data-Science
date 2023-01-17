import pandas as pd

# Simple Dataframe (Bugatti Models)
car_data = {
    "model" : ["Veyron", "Chiron", "Divo", "Bolide"],
    "top_speed" : [410, 440, 380, 498]
}
car_df = pd.DataFrame(car_data)
print(car_df)

# Access Row
print(car_df.loc[0])

# Access Multiple Rows
print(car_df.loc[[0,1,2]])

# Named Indexes
car_indexed_df = pd.DataFrame(car_data, index = ["car1", "car2", "car3", "car4"])
print(car_indexed_df)

# Access Named Row
print(car_indexed_df.loc["car1"])