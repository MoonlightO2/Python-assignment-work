import pandas as pd
import folium

# grow_data1 = []

grow_data1 = pd.read_csv('GrowLocations.csv')
print("Grow dataset 1 - Shape")
print(grow_data1.shape)

print("Grow dataset 1 - First 5 rows of dataset")
print(grow_data1.head())
print("Grow dataset 1 - Whole dataset")
print(grow_data1)

print("Show all columns: that contains Null values....")
print(grow_data1.isna().sum())

print("\nRemoving all columns that contains Null values....")
grow_data2 = grow_data1.drop(grow_data1.columns[grow_data1.apply(lambda col:col.isna().sum() > 3)], axis=1)

# grow_data2 = []

# Removing only Null values - Columns
grow_data2 = grow_data1.dropna(subset=['Serial'])
print("\nGrow dataset 2 - Shape")
print(grow_data2.shape)
print("\nShow all columns....")
print(grow_data2.isna().sum())
print("\nGrow dataset 2")
print(grow_data2.head())

# grow_data3 = []

print("\nRemoving only Null values - Rows....")
grow_data3 = grow_data2.dropna()
print(grow_data3.isna().sum())
print("\nGrow dataset 3 - Shape")
print(grow_data3.shape)
print("\nGrow dataset 3")
print(grow_data3.head())

"""
print("Cleaning Coordinates....")
lng = grow_data1.dropna(subset=['Longitude'])
lat = grow_data1.dropna(subset=['Latitude'])

print(lat, lng)

"""
grow_data4 = []

grow_data4 = grow_data3[(grow_data3.Latitude != 0) & (grow_data3.Longitude != 0)]
print("\nGrow dataset 4 - Shape")
print(grow_data4.shape)
print("\nGrow dataset 4 - with zeros")
print(grow_data4.head())
print("Removing null values in Coordinates....")
print(grow_data4.notnull().sum())
grow_data5 = grow_data4.notnull()
print("\nGrow dataset 5 - Shape")
print(grow_data5.shape)
print("\nGrow dataset 5 - No nulls")
print(grow_data5.head())
"""


# map = folium.Map(location=[grow_data4.Latitude, grow_data4.Longitude], zoom_start=14, control_scale=True)

# map = folium.Map(location=[grow_data5.Latitude, grow_data5.Longitude], zoom_start=14, control_scale=True)

"""
print("Removing Duplicate values in rows....")
grow_data4 = grow_data3.drop_duplicates
print(grow_data4.isna().sum())
print("\nGrow dataset 4 - Shape")
print(grow_data3.shape)
print("\nGrow dataset 4 - without Duplicates")
print(grow_data4)

b = grow_data3.select_dtypes(exclude="String")
print("Print without FALSE")
print(b)
print("Null values removed...")

print("Creating map.....")
map.save("map.html")
print("Map created.....")

folium.PolyLine(locations=[(56.47386042203257, -2.964379206760871), (56.47386042203257, -2.964379206760871)], line_opacity=8.6).add_to(map)
folium.CircleMarker(location=[grow_data.Latitude.mean(), grow_data.Longitude.mean()], radius=50, popup="anyplace2").add_to(map)
folium.Marker([grow_data.Latitude.mean(), grow_data.Longitude.mean()], popup="unknown place").add_to(map)


#webbrowser.open("https://www.google.com/maps/place/" + input("Enter your location: "))
"""