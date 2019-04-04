import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
location=list(data["LOCATION"])
status=list(data["STATUS"])
elev=list(data["ELEV"])

def decide_color(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

def fillcolor(x):
    if x["properties"]["POP2005"]<10000000:
        return {"fillColor":"green"}
    elif 10000000<=x["properties"]["POP2005"]<20000000:
        return {"fillColor":"yellow"}
    elif 20000000<=x["properties"]["POP2005"]<30000000:
        return {"fillColor":"orange"}
    else:
        return {"fillColor":"red"}

lat_total=0
for i in lat:
    lat_total=lat_total+i
lat_average=lat_total/len(lat)

lon_total=0
for i in lon:
    lon_total=lon_total+i
lon_average=lon_total/len(lon)

map=folium.Map(location=[lat_average,lon_average], zoom_start=4, tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="Volcanoes")

for i in range(0,len(data)):
    fgv.add_child(folium.Marker(location=[lat[i],lon[i]],popup=str(elev[i])+" m ", icon=folium.Icon(color=decide_color(elev[i]), icon_color="white")))
"""
folium.CircleMarker for circle marker
"""
map.add_child(fgv)

fgp=folium.FeatureGroup(name="Population level")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),style_function=fillcolor))
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

