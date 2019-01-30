from petproject import DataModel as dm, DataView as dv


class DataController(object):

    def __init__(self):
        pass

    def update_view(self):
        dv.DataView(dm.DataModel().get_activities()).get_map()
