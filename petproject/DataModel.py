import codecs
import json
import os

import pandas as pd
import requests as r
from jsonmerge import merge

from petproject import StravaSetup as strs


class DataModel(object):

    def __init__(self):
        self.auth_url1 = 'https://www.strava.com/api/v3/athlete/activities'
        self.auth_url2 = 'https://www.strava.com/api/v3/activities'
        self.auth_header = {'Authorization': strs.authorization}

    def get_activities(self):
        print("Hello user!")

        if os.path.isdir('files') == False:
            os.mkdir('files')
            print('made data files')
        else:
            print('files dir already availabale')

        if os.path.isdir('files/data') == False:
            os.mkdir('files/data')
            print('made data dir')
        else:
            print('data dir already availabale')

        if os.path.isdir('files/map') == False:
            os.mkdir('files/map')
            print('made map dir')
        else:
            print('data map already availabale')

        if os.path.isfile('./files/data/activities.json') == False:
            print("generate json files")

            json_data = r.get(self.auth_url1, headers=self.auth_header).json()

            with codecs.open('./files/data/activities.json', 'w', 'utf8') as f:
                f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

            print('made json file')
        else:
            print("json already available")

        if os.path.isfile('./files/data/activities.xlsx') == False:
            print("generate xlsx files")
            pd.read_json("./files/data/activities.json").to_excel("./files/data/activities.xlsx")
            print('made xlsx file')
        else:
            print("xlsx already available")
        # df = pd.read_excel('./files/data/activities.xlsx')
        # df = df.dropna(subset=['start_latitude', 'start_longitude'], how='any')
        # df = df.rename(index=str, columns={'start_latitude': 'lat', 'start_longitude': 'lng'})

        df = pd.read_excel('./files/data/activities.xlsx') \
            .dropna(subset=['start_latitude', 'start_longitude'], how='any') \
            .rename(index=str, columns={'start_latitude': 'lat', 'start_longitude': 'lng'})

        for index, row in df.iterrows():
            json_data2 = r.get(self.auth_url2 + '/' + str(row['id']), headers=self.auth_header).json()
            # json_data = r.get(self.auth_url1, headers=self.auth_header).json()

            with codecs.open('./files/data/activity_details_' + str(row['id']) + '.json', 'w', 'utf8') as f:
                f.write(json.dumps(json_data2, sort_keys=True, ensure_ascii=False))

            result = None
            result = merge(result, json_data2)

            with codecs.open('./files/data/activity_details.json', 'w', 'utf8') as f:
                f.write(json.dumps(result, sort_keys=True, ensure_ascii=False))

        # pd.read_json('./files/data/activity_details.json').to_excel('./files/data/activity_details.xlsx')
        # print(pd.DataFrame.from_dict(result, orient='index'))

        return df
