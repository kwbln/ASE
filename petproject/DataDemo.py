from petproject import DataController as dc


class DataDemo(object):

    def __init__(self):
        self.success = 'Oh... the demo failed...'

    def main(self):
        try:
            # creates a controller and runs the update method
            my_data_controller = dc.DataController()
            my_data_controller.update_views()
            self.success = 'Yeah! Great demo!'
            print(self.success)
        except Exception:
            print(self.success)


DataDemo().main()
