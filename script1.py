import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")


map=folium.Map(location=[45.372, -121.697],zoom_start=4, tiles='Stamen Terrain')


for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker([lat,lon], popup=name, icon=folium.Icon(color='green' if elev in range(0,1000)else 'orange' if elev in range(1000,3000) else 'red')).add_to(map)

#map.add_child(folium.Marker(location=[45.3288, -121.6625], popup='Mt. Hood Meadows', icon=folium.Icon(color='white',icon_color='red')) )
map.save('test.html')
