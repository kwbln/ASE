import os

import setup

import Presenter as p


def test():
    return 'test'


def main():
    header = {'Authorization': setup.authorization}
    os.chdir(setup.working_dir)

    x = p.Presenter()
    x.generate_all_activities_data(header)


    # os.chdir(setup.working_dir)
    # header = {'Authorization': setup.authorization}
    #
    # print("Hello user!")
    # print("Generate some files...")

    # generate_profile_data(header)
    # generate_athletes_data(header)
    # generate_single_activity_data(header)
    # generate_laps_data(header)
    # generate_all_activities_data(header)
    #
    # print("Done!")

    # print("------------------")
    # print("1 - use sample activities")
    # print("2 - use your own activities")
    # var = input()
    # print("You entered " + str(var))
#
#
# def generate_profile_data(header):
#     ath_url = 'https://www.strava.com/api/v3/athlete'
#     json_data = r.get(ath_url, headers=header).json()
#
#     with codecs.open('_files_/_1 JSON_/profile_data.json', 'w', 'utf8') as f:
#         f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))
#     # for key, value in json_data.items():
#     #    print(key + ':', value)
#
#
# def generate_athletes_data(header):
#     ath_url = 'https://www.strava.com/api/v3/athletes/' + setup.athlet_id + '/stats?per_page=30'
#     json_data = r.get(ath_url, headers=header).json()
#
#     with codecs.open('_files_/_1 JSON_/athlet_data.json', 'w', 'utf8') as f:
#         f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))
#     # for key, value in json_data.items():
#     #    print(key + ':', value)
#
#
# def generate_single_activity_data(header, activity_id=setup.activity_id):
#     ath_url = 'https://www.strava.com/api/v3/activities/' + activity_id
#     json_data = r.get(ath_url, headers=header).json()
#     # print(json_data)
#     # print(type(json_data))
#     # for key, value in json_data.items():
#     #    print(key + ':', value)
#     with codecs.open('_files_/_1 JSON_/activity_data.json', 'w', 'utf8') as f:
#         f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))
#
#
# def generate_laps_data(header, activity_id=setup.activity_id):
#     ath_url = 'https://www.strava.com/api/v3/activities/' + activity_id + '/laps'
#     json_data = r.get(ath_url, headers=header).json()
#     # print(json_data)
#     # print(type(json_data))
#     # for key, value in json_data.items():
#     #    print(key + ':', value)
#     with codecs.open('_files_/_1 JSON_/laps_data.json', 'w', 'utf8') as f:
#         f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))


# def generate_all_activities_data(header):
#     ath_url = 'https://www.strava.com/api/v3/athlete/activities?per_page=30'
#
#     json_data = r.get(ath_url, headers=header).json()
#
#     with codecs.open('_files_/_1 JSON_/activities_data.json', 'w', 'utf8') as f:
#         f.write(json.dumps(json_data, sort_keys=True, ensure_ascii=False))


main()
