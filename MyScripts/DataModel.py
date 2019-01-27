import codecs
import json
import os

import pandas as pd
import requests as r

import strava_setup as strs


class DataModel(object):

    def __init__(self):
        pass

    def getActivities(self):
        print("Hello user!")

        authheader = {'Authorization': strs.authorization}

        if os.path.isdir('data') == False:
            os.mkdir('data')
            print('made data dir')
        else:
            print('data dir already availabale')

        if os.path.isdir('map') == False:
            os.mkdir('map')
            print('made map dir')
        else:
            print('data map already availabale')

        if os.path.isfile('./data/activities.json') == False:
            print("generate json files")
            ath_url = 'https://www.strava.com/api/v3/athlete/activities?per_page=30'
            json_data = r.get(ath_url, headers=authheader).json()

            with codecs.open('./data/activities.json', 'w', 'utf8') as f:
                f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

            print('made json file')
        else:
            print("json already available")

        if os.path.isfile('./data/activities.xlsx') == False:
            print("generate xlsx files")
            pd.read_json("./data/activities.json").to_excel("./data/activities.xlsx")
            print('made xlsx file')
        else:
            print("xlsx already available")

        return pd.read_excel('./data/activities.xlsx').dropna(subset=['start_latitude', 'start_longitude'], how='any')
