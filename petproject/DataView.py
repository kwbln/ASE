import folium


class DataView(object):
    def __init__(self):
        # some fix values: center and filepath of the map
        self.center = [52.5348302, 13.4720917]
        self.map_name = './files/map/my_map.html'

    def get_map(self, dataframe):
        # some map settings
        tiles = 'Stamen Terrain' # Mapbox Bright, Stamen Toner, Mapbox Control Room, OpenStreetMap, ...
        zoom_start = 12
        color = 'darkred'
        icon = 'circle'

        try:
            # creates the map, gps markers and saves the map
            my_map = folium.Map(location=self.center, tiles=tiles, zoom_start=zoom_start)

            for index, row in dataframe.iterrows():
                folium.Marker(location=[row['lat'], row['lng']],
                              icon=folium.Icon(color=color, icon=icon)).add_to(my_map)

            my_map.save(self.map_name)

        except Exception:
            print("An error occured - DataView - get_map()")

    def get_heatmap(self):
        # --- to be implemented ---
        pass

    def get_chart(self):
        # --- to be implemented ---
        pass
