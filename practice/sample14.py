import googlemaps
import folium

# gmaps_key = "AIzaSyBo9Ro047DFTo4ua8PoU8e2A6VfydYPvhY"
# gmaps = googlemaps.Client(key=gmaps_key)
# gmaps.geocode('대한민국 서울특별시 강남구 대치2동 514',language='ko')
# a = folium.Map(location=[45.5236,-122.6750])

map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
folium.Marker([37.566345, 126.977893], popup='서울특별시청', icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
folium.CircleMarker([37.5658859, 126.9754788], radius=100,color='#3186cc',fill_color='#3186cc', popup='덕수궁').add_to(map_osm)
# map_osm.save('c:/app/py_workspace/map6.html')

import webbrowser
# webbrowser.open(map_osm._repr_html_())
