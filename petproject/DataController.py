from petproject import DataModel as dm, DataView as dv


class DataController(object):

    def __init__(self, name):
        self.name = name

    def update_view(self):
        try:
            dv.DataView(dm.DataModel().get_activities()).get_map()

        except Exception:
            print("An error occured - DataController - update_view()")
