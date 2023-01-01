import pandas as pd
import folium

city_data1 = pd.read_csv('world_cities2.csv')
print("World Cities dataset 1 - Shape")
print(city_data1.shape)

map = folium.Map(location=[city_data1.lat, city_data1.lng], zoom_start=14, control_scale=True)
folium.CircleMarker(location=[city_data.lat.mean(), city_data.lng.mean()], radius=50, popup="anyplace2").add_to(map)
folium.Marker([city_data.lat.mean(), city_data.lng.mean()], popup="unknown place").add_to(map)
folium.PolyLine(locations=[(city_data1.lat, city_data1.lng), (city_data1.lat, city_data1.lng)], line_opacity=8.6).add_to(map)

map.save("mappy.html")
print("Map created.....")
