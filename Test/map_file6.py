import pandas as pd
import numpy as np

data = pd.read_csv("GrowLocations.csv")
print(data.dtypes)
print(data['Latitude'].dtype)
print(data['Longitude'].dtype)

data['Latitude'] = data['Latitude'].astype(int)
data['Longitude'] = data['Longitude'].astype(int)

print(data.dtypes)
print(data['Latitude'].dtype)
print(data['Longitude'].dtype)
