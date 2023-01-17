import pandas as pd

# Simple Pandas Series
odd_array = [1, 3, 5, 7, 9]
pandas_odd_series = pd.Series(odd_array)
print(pandas_odd_series) 

# Default Label Access
print(str(pandas_odd_series[0]))

# Custom Labels
even_array = [2, 4, 6, 8, 10]
pandas_even_series = pd.Series(even_array, index = ["Two", "Four", "Six", "Eight", "Ten"])
print(pandas_even_series)

# Custom Label Access
print(pandas_even_series["Two"])

# Key/Value Objects
fuel_dictionary = {"day1" : 100, "day2" : 85, "day3" : 50}
pandas_fuel_series_1 = pd.Series(fuel_dictionary)
print(pandas_fuel_series_1)

# Specify Data To Be Added
pandas_fuel_series_2 = pd.Series(fuel_dictionary, index = ["day1", "day2"])
print(pandas_fuel_series_2)
