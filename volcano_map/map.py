import folium
import pandas

data = pandas.read_csv('volcanoes_world.txt')
lat = list(data['Latitude'])
lon = list(data['Longitude'])
high = list(data['Elev'])


def color_check(elevation):
    if elevation < 4000:
       return 'green'
    elif 4000 <= elevation <= 6000:
        return 'orange'
    else:
        return 'red'


map1 = folium.Map(location=[59.9, 30.3], tiles='openstreetmap')
fg_v = folium.FeatureGroup(name='Volcanoes')

for lt,ln, hg in zip(lat,lon, high):
    if hg > 3000.0:
        fg_v.add_child(folium.CircleMarker(
            location=[lt,ln], 
            radius = 6, 
            popup=str(hg) + 'm', 
            fill_color=color_check(hg), 
            fill_opacity = 0.9, 
            color = 'grey'
            ))

fg_p = folium.FeatureGroup(name='Population')
fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
                                                    else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))                                                   

map1.add_child(fg_v)
map1.add_child(fg_p)
map1.add_child(folium.LayerControl())
map1.save('Map1.html')