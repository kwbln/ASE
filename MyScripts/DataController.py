import DataModel as dm
import DataView as dv


class DataController(object):

    def __init__(self):
        pass

    def update_view(self):
        my_data = dm.DataModel()
        my_df = my_data.get_activities()

        my_dv = dv.DataView()
        my_dv.get_map(my_df)
