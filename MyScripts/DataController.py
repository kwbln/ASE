import DataModel as dm
import DataView as dv


class DataController(object):

    def __init__(self):
        pass

    def updateView(self):
        my_data = dm.DataModel()
        my_df = my_data.getActivities()

        my_dv = dv.DataView()
        my_dv.getMap(my_df)
