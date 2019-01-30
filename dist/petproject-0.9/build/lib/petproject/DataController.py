from petproject import DataModel as dm, DataView as dv, StravaSetup as strs


class DataController(object):

    def __init__(self):
        self.auth_url = 'https://www.strava.com/api/v3/athlete/activities?per_page=30'
        self.auth_header = {'Authorization': strs.authorization}
        self.center = [52.5348302, 13.4720917]

    def update_view(self):
        dv.DataView(self.center, dm.DataModel(self.auth_url, self.auth_header).get_activities())
