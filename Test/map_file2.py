import folium

# initialize a map with center and zoom
mapObj = folium.Map(location=[56.47386042203257, -2.964379206760871],
                     zoom_start=8, tiles=None)

# add tile layers
folium.TileLayer('openstreetmap').add_to(mapObj)
folium.TileLayer('stamenterrain', attr="stamenterrain").add_to(mapObj)
folium.TileLayer('stamenwatercolor', attr="stamenwatercolor").add_to(mapObj)
folium.TileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', name='CartoDB.DarkMatter', attr="CartoDB.DarkMatter").add_to(mapObj)

# add layers control over the map
folium.LayerControl().add_to(mapObj)

# save the map as html file
print("Creating map.....")
mapObj.save("map.html")
print("Map created.....")

