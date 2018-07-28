import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def colour_producer(elevation):
    if elevation < 1500:
        return "green"
    elif elevation < 3000 and elevation >= 1500:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.3, -99.01], zoom_start="6", tiles="MapBox Bright")
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=str(el) + "m", icon=folium.Icon(color=colour_producer(el))))
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {"fillColor": "orange" if x["properties"]["POP2005"] < 1000000
                             else "green" if x["properties"]["POP2005"] < 2000000 else "red"}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map4.html")
