import folium
from folium.plugins import MarkerCluster
import pandas as pd

# Load data
data = pd.read_csv("Nuclear_Waste_Sites_on_US_Campuses.csv")
lat = data['lat']
lon = data['lon']
name = data['text']

# Create a base map
map = folium.Map(location=[37.000000,-96.000000], zoom_start=4.5, tiles="openstreetmap")

# To create clusters
#markercluster = MarkerCluster().add_to(map)

# Add all markers
for lat, lon, name in zip(lat, lon, name):
    folium.CircleMarker(location=[lat, lon], radius=9, popup=str(name),
                  fill_color="red", color="black", fill_opacity=0.9).add_to(map)
#    folium.CircleMarker(location=[lat, lon], radius=9, popup=str(name),
#                  fill_color="red", color="black", fill_opacity=0.9).add_to(markercluster)

title_html =   '''
                <div style="position: fixed; 
                            bottom: 50px; left: 50px; width: 300px; height: 30px; 
                            border:2px solid black; z-index:9999; font-size:16px;
                            color:red">&nbsp; Nuclear Waste Sites on US Campuses
                </div>
                '''

map.get_root().html.add_child(folium.Element(title_html))

map.save("map_nuclear_on_us_campus.html")
