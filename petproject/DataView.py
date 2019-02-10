import folium


class DataView(object):
    def __init__(self, dataframe):
        self.center = [52.5348302, 13.4720917]
        self.df = dataframe
        self.map_name = './files/map/my_map.html'

    def get_map(self):
        try:
            map = folium.Map(location=self.center, tiles='Stamen Terrain', zoom_start=12)

            for index, row in self.df.iterrows():
                folium.Marker(location=[row['lat'], row['lng']],
                              icon=folium.Icon(color='darkred', icon='circle')).add_to(map)

            map.save(self.map_name)

        except Exception:
            print("An error occured - DataView - get_map()")

    def get_heatmap(self):
        # not part of the current version
        pass

    def get_chart(self):
        # not part of the current version
        pass
