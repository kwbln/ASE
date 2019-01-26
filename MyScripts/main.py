import Preparator as prep
import Presenter as pres
import strava_setup as strs


def test():
    return 'test'


def main():

    header = {'Authorization': strs.authorization}

    my_prep = prep.Preparator()
    my_df = my_prep.generate_all_activities_data(header)\
        .dropna(subset=['start_latitude', 'start_longitude'], how='any')

    my_pres = pres.Presenter()

    my_pres.create_map(my_df)


main()
