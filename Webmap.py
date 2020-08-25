import folium
import pandas

data = pandas.read_csv("files\Volcano.txt")
lat = list(data["LAT"])
long = list(data["LON"])
volcano_name = list(data["NAME"])
volcano_loc = list(data['LOCATION'])
elev = list(data['ELEV'])

def color_producer (elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 < elevation < 2000:
        return 'yellow'
    elif 2000 < elevation < 3000:
        return 'orange'
    else:
        return 'red'

html = '''
Volcano Name:<br>
<a href = "https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
'''

map = folium.Map(location=[34.05, -84.53], zoom_start=5, tiles = "Stamen Terrain")
fgp = folium.FeatureGroup(name = "World Population data")
fgv = folium.FeatureGroup(name = "US Volcanoes")

#popup may give blank webpage if ' is in string or when converting from float/int to str. correct with code below
#popup = folium.Popup (str(el), parse_html = True)

for lat, lon, name, el in zip (lat, long, volcano_name, elev):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100,)
    #below is normal map markers
    #fgv.add_child(folium.Marker(location=[lat, lon], popup =folium.Popup(iframe), icon = folium.Icon(color=color_producer(el))))
    #below is circle dot markers
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius= 8, popup =folium.Popup(iframe), fill_color=color_producer(el), color = 'black', fill_opacity=0.7 ))

fgp.add_child(folium.GeoJson(data=open('files\world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'blue' if 10000000 < x['properties']['POP2005'] < 100000000 else 'orange'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save ("Map1.html")
