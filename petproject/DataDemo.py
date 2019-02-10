from petproject import DataController as dc


class DataDemo(object):

    def __init__(self):
        self.success = 'Oh... the demo failed...'

    def main(self):
        try:
            dc.DataController('MyController').update_view()
            self.success = 'Yeah! Great demo!'
            print(self.success)
        except Exception:
            print(self.success)


DataDemo().main()
