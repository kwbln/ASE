import codecs
import json
import os

import pandas as pd
import requests as r
from jsonmerge import merge

from petproject import StravaSetup as strs


class DataModel(object):

    def __init__(self):
        self.auth_url1 = 'https://www.strava.com/api/v3/athlete/activities?per_page=1000'
        self.auth_url2 = 'https://www.strava.com/api/v3/activities'
        self.auth_header = {'Authorization': strs.authorization}

    def get_activities(self):
        try:
            # checks for the necessary directories
            if os.path.isdir('files') == False:
                os.mkdir('files')

            if os.path.isdir('files/data') == False:
                os.mkdir('files/data')

            if os.path.isdir('files/map') == False:
                os.mkdir('files/map')

            # checks for the json file - gets the data if not already available and saves as xlsx
            if os.path.isfile('./files/data/activities.json') == False:
                json_data = r.get(self.auth_url1, headers=self.auth_header).json()

                with codecs.open('./files/data/activities.json', 'w', 'utf8') as f:
                    f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

            if os.path.isfile('./files/data/activities.xlsx') == False:
                pd.read_json("./files/data/activities.json").to_excel("./files/data/activities.xlsx")

            # some playing with the excel: drop the NaN in start_lat and start_lng and rename the columns
            my_data = pd.read_excel('./files/data/activities.xlsx') \
                .dropna(subset=['start_latitude', 'start_longitude'], how='any') \
                .rename(index=str, columns={'start_latitude': 'lat', 'start_longitude': 'lng'})

            # gets more data about the activities and saves them in single json files, also merges them into one file
            for index, row in my_data.iterrows():
                json_data2 = r.get(self.auth_url2 + '/' + str(row['id']), headers=self.auth_header).json()

                with codecs.open('./files/data/activity_details_' + str(row['id']) + '.json', 'w', 'utf8') as f:
                    f.write(json.dumps(json_data2, sort_keys=True, ensure_ascii=False))

                result = None
                result = merge(result, json_data2)

                with codecs.open('./files/data/activity_details.json', 'w', 'utf8') as f:
                    f.write(json.dumps(result, sort_keys=True, ensure_ascii=False))

            return my_data
        except Exception:
            print("An error occured - DataModel - get_activities()")
