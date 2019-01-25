import codecs
import json
import os

import pandas as pd
import requests as r


class Preparator(object):

    def __init__(self):
        pass

    def generate_all_activities_data(self, header):
        print("Hello user!")

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

        if os.path.isfile('./data/abc.json') == False:
            print("generate json files")
            ath_url = 'https://www.strava.com/api/v3/athlete/activities?per_page=30'
            json_data = r.get(ath_url, headers=header).json()

            # with codecs.open('_files_/_JSON_/activities_data.json', 'w', 'utf8') as f:
            with codecs.open('./data/abc.json', 'w', 'utf8') as f:
                f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

            print('made json file')
        else:
            print("json already available")

        if os.path.isfile('./data/abc.xlsx') == False:
            print("generate xlsx files")
            pd.read_json("./data/abc.json").to_excel("./data/abc.xlsx")
            print('made xlsx file')
        else:
            print("xlsx already available")

        return pd.read_excel('./data/abc.xlsx')
        #
        # inputFile = open('abc.json')  # open json file
        #
        # outputFile = open('abc.csv', 'w')  # load csv file
        # data = json.load(open('abc.json'))  # load json content
        # inputFile.close()  # close the input file
        #
        # output = csv.writer(outputFile)  # create a csv.write
        #
        # output.writerow(data[0].keys())  # header row
        #
        # for row in data:
        #     output.writerow(row.values())  # values row

        # output_data = pd.read_csv("abc.csv", error_bad_lines=False)

        # output_data.sample(5)
