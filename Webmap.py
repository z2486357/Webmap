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

lat_total=0
for i in lat:
    lat_total=lat_total+i
lat_average=lat_total/len(lat)

lon_total=0
for i in lon:
    lon_total=lon_total+i
lon_average=lon_total/len(lon)

map=folium.Map(location=[lat_average,lon_average], zoom_start=7, tiles="Mapbox Bright")

for i in range(0,len(data)):
    map.add_child(folium.Marker(location=[lat[i],lon[i]],popup=str(elev[i])+" m ", icon=folium.Icon(color=decide_color(elev[i]), icon_color="white")))
"""
folium.CircleMarker for circle marker
"""
map.save("Map1.html")

