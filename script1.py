import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")


map=folium.Map(location=[45.372, -121.697],zoom_start=4, tiles='Stamen Terrain')


for lat, lon, name in zip(df['LAT'], df['LON'], df['NAME']):
    folium.Marker([lat,lon], popup=name, icon=folium.Icon(color='red')).add_to(map)

#map.add_child(folium.Marker(location=[45.3288, -121.6625], popup='Mt. Hood Meadows', icon=folium.Icon(color='white',icon_color='red')) )

# folium.Marker([45.3311, -121.7113],
# popup='Timberline Lodge',
# icon=folium.Icon(color='green')
# ).add_to(map)

map.save('test.html')
