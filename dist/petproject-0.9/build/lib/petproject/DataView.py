import folium


class DataView(object):
    def __init__(self, center, dataframe):
        self.center = center
        self.df = dataframe

    def get_map(self):
        m = folium.Map(location=self.center, tiles='Stamen Terrain', zoom_start=12)

        for index, row in self.df.iterrows():
            folium.Marker(location=[row['start_latitude'], row['start_longitude']],
                          icon=folium.Icon(color='darkred', icon='circle')).add_to(m)

        m.save('./files/map/my_map.html')

        print('map saved')

    def get_heatmap(self):
        pass

    def get_chart(self):
        pass
