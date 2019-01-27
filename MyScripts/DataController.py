import DataModel as dm
import DataView as dv
import strava_setup as strs


class DataController(object):

    def __init__(self):
        self.auth_url = 'https://www.strava.com/api/v3/athlete/activities?per_page=30'
        self.auth_header = {'Authorization': strs.authorization}
        self.center = [52.5348302, 13.4720917]

    def update_view(self):

        #my_data = dm.DataModel(self.auth_url, self.auth_header)
        #my_df = my_data.get_activities()

        #my_dv = dv.DataView(self.center , my_df)
        #my_dv.get_map()

        dv.DataView(self.center, dm.DataModel(self.auth_url, self.auth_header).get_activities())

