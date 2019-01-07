import codecs
import json

import requests as r


class Presenter(object):

    def __init__(self):
        pass

    def generate_all_activities_data(header):
        print("Hello user!")
        print("Generate some files...")
        ath_url = 'https://www.strava.com/api/v3/athlete/activities?per_page=30'

        json_data = r.get(ath_url, headers=header).json()

        with codecs.open('_files_/_JSON_/activities_data.json', 'w', 'utf8') as f:
            f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

        print("Generate some files...")
