import folium


class Presenter(object):

    def __init__(self):
        pass

    def create_map(self, df):
        m = folium.Map(location=[52.5348302, 13.4720917], tiles='Stamen Terrain', zoom_start=12)

        for index, row in df.iterrows():
            # folium.CircleMarker(location=[row['start_latitude'], row['start_longitude']], radius=5, color='red').add_to(
            # m)
            folium.Marker(location=[row['start_latitude'], row['start_longitude']],
                          icon=folium.Icon(color='darkred', icon='circle')).add_to(m)

        m.save('./map/my_map.html')

        print('map saved')
