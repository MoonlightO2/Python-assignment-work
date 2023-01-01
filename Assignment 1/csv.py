import pandas as pd
#import folium

grow_data = pd.read_csv(r'GrowLocations.csv')
print(grow_data)

"""
map = folium.Map(location=[56.47386042203257, -2.964379206760871], tiles="Stamen Terrain", zoom_start=15)
folium.CircleMarker(location=[56.47386042203257, -2.964379206760871], radius=50, popup="anyplace2").add_to(map)
folium.Marker([56.47386042203257, -2.964379206760871], popup="unknown place").add_to(map)
folium.PolyLine(locations=[(56.47386042203257, -2.964379206760871), (56.47386042203257, -2.964379206760871)], line_opacity=8.6).add_to(map)

print("Creating map.....")
map.save("map.html")
print("Map created.....")

#webbrowser.open("https://www.google.com/maps/place/" + input("Enter your location: "))
"""