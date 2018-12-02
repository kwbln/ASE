import requests as r
import codecs, json, os
import setup

def main():
    os.chdir(setup.working_dir)
    access_token = setup.access_token
    header = {'Authorization': setup.authorization}

    print("Hello user!")
    print("Generate some files...")

    generate_athletes_data(header)
    generate_single_activity_data(header)
    generate_all_activities_data(header)

    print("Done!")

    #print("------------------")
    #print("1 - use sample activities")
    #print("2 - use your own activities")
    #var = input()
    #print("You entered " + str(var))

def generate_athletes_data(header):
    ath_url = 'https://www.strava.com/api/v3/athletes/' + setup.athlet_id + '/stats?per_page=30'
    json_data = r.get(ath_url, headers=header).json()

    with codecs.open('Data/1 Generated/athlet_data.json', 'w', 'utf8') as f:
        f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))
    #for key, value in json_data.items():
    #    print(key + ':', value)

def generate_single_activity_data(header, activity_id = setup.activity_id):
    ath_url = 'https://www.strava.com/api/v3/activities/' + activity_id
    json_data = r.get(ath_url, headers=header).json()
    # print(json_data)
    # print(type(json_data))
    # for key, value in json_data.items():
    #    print(key + ':', value)
    with codecs.open('Data/1 Generated/activity_data.json', 'w', 'utf8') as f:
        f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

def generate_all_activities_data(header):
    ath_url = 'https://www.strava.com/api/v3/athlete/activities?per_page=30'

    json_data = r.get(ath_url, headers=header).json()

    with codecs.open('Data/1 Generated/activities_data.json', 'w', 'utf8') as f:
        f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))

#dfCountries = show_countries(df)
#print(dfCountries)

main()

