import folium


class DataView(object):
    def __init__(self):
        self.center = [52.5348302, 13.4720917]

    def getMap(self, df):
        m = folium.Map(location=self.center, tiles='Stamen Terrain', zoom_start=12)

        for index, row in df.iterrows():
            folium.Marker(location=[row['start_latitude'], row['start_longitude']],
                          icon=folium.Icon(color='darkred', icon='circle')).add_to(m)

        m.save('./map/my_map.html')

        print('map saved')

    def getHeatmap(self):
        pass

    def getActivityChart(self):
        pass
