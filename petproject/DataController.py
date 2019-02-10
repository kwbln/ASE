from petproject import DataModel as dm, DataView as dv


class DataController(object):

    def __init__(self):
        # the controller creates a model and a view
        self.model = dm.DataModel()
        self.view = dv.DataView()

    def update_views(self):
        try:
            my_dataframe = self.model.get_activities()
            self.view.get_map(my_dataframe)

            # --- to be implemented ---
            # self.view.get_heatmap(my_dataframe)
            # self.view.get_chart(my_dataframe)
        except Exception:
            print("An error occured - DataController - update_view()")
