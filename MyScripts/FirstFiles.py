import pandas as pd
import os

def main():
    print("Hello user!")
    print("What you wanna do?")
    print("------------------")
    print("1 - use sample activities")
    print("2 - use your own activities")
    var = input()
    print("You entered " + str(var))

def generate_sample():
    #cwd = os.getcwd()
    os.chdir('C:/Users/kwagn/Github/ASE/venv/') # have to set the directory in the build
    #cwd = os.getcwd()
    df = pd.read_csv('Include/Data/0 Raw samples/FakeNameGenerator_com.csv', sep=',')
    return df

def show_countries(df):
    countries = df.Country.unique()
    return countries

#df = generate_sample()
#print(generate_sample())

#dfCountries = show_countries(df)
#print(dfCountries)

main()

