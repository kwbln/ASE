import codecs
import json
import os

import pandas as pd
import requests as r


class DataModel(object):

    def __init__(self, auth_url, auth_header):
       self.auth_url = auth_url
       self.auth_header = auth_header

    def get_activities(self):
        print("Hello user!")

        if os.path.isdir('things') == False:
            os.mkdir('things')
            print('made data things')
        else:
            print('things dir already availabale')

        if os.path.isdir('things/data') == False:
            os.mkdir('things/data')
            print('made data dir')
        else:
            print('data dir already availabale')

        if os.path.isdir('things/map') == False:
            os.mkdir('things/map')
            print('made map dir')
        else:
            print('data map already availabale')

        if os.path.isfile('./things/data/activities.json') == False:
            print("generate json files")

            json_data = r.get(self.auth_url, headers=self.auth_header).json()

            with codecs.open('./things/data/activities.json', 'w', 'utf8') as f:
                f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

            print('made json file')
        else:
            print("json already available")

        if os.path.isfile('./things/data/activities.xlsx') == False:
            print("generate xlsx files")
            pd.read_json("./things/data/activities.json").to_excel("./things/data/activities.xlsx")
            print('made xlsx file')
        else:
            print("xlsx already available")

        return pd.read_excel('./things/data/activities.xlsx') \
            .dropna(subset=['start_latitude', 'start_longitude'], how='any')
