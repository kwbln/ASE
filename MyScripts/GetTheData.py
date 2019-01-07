import requests
import os
import sys
import csv
import setup

token = os.chdir(setup.working_dir)
headers = {'Authorization': setup.authorization}


with open("runs.csv", "w") as runs_file:
    writer = csv.writer(runs_file, delimiter=",")
    writer.writerow(["id", "polyline"])

    page = 1
    while True:
        r = requests.get("https://www.strava.com/api/v3/athlete/activities?page={0}".format(page), headers = headers)
        response = r.json()

        if len(response) == 0:
            break
        else:
            for activity in response: #if key in dict
                r = requests.get("https://www.strava.com/api/v3/activities/{0}?include_all_efforts=true".format(activity["id"]), headers = headers)
                polyline = r.json()["map"]["polyline"]
                writer.writerow([activity["id"], polyline])
                print([activity["id"], polyline])
            page += 1




