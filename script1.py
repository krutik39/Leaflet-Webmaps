import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")


map=folium.Map(location=[df['LAT'].mean(), df['LON'].mean()],zoom_start=6, tiles='Mapbox Bright')

def color(elev):
    minimum = int(min(df['LAT']))
    step=int((max(df['ELEV'])-min(df['ELEV']))/3)
    if elev in range(minimum,minimum+step):
        col='green'
    elif elev in range(minimum+step,minimum+step*2):
        col='orange'
    else:
        col='red'
    return col



# for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
#     folium.Marker([lat,lon], popup=name, icon=folium.Icon(color=color(elev),icon_color='gold')).add_to(map)

# folium.GeoJson(data=open('World_population.json'),
# name = 'World Population',
# style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000< x['properties']['POP2005']<20000000 else 'red'}).add_to(map)

fg = folium.FeatureGroup(name='Volcano Locations')

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    map.add_child(folium.Marker([lat,lon], popup=name, icon=folium.Icon(color=color(elev),icon_color='gold')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('World_population.json'),
name = 'World Population',
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000< x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(folium.LayerControl())



#map.add_child(folium.Marker(location=[45.3288, -121.6625], popup='Mt. Hood Meadows', icon=folium.Icon(color='white',icon_color='red')) )
map.save('test.html')
