import folium

mapa =  folium.Map().add_child(
    folium.ClickForMarker()
)

mapa.save("mapa_ciudadano.html")