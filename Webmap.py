import folium

map=folium.Map(location=[38.58,-99.09], zoom_start=6)
for i in [[38.59,-99.15],[38.25,-99.35]]:
    map.add_child(folium.Marker(location=i,popup="I am a marker!!!", icon=folium.Icon(color="red", icon_color="green")))
map.save("Map1.html")