import data
import statistics
import districts
import sys


def main(argv):

    covid_data=data.Data(argv[1])
    district_data=districts.Districts(covid_data)
    district_data.filter_districts(["L","S"])

    print("Question 1:")
    actions=[statistics.mean,statistics.median]
    features=["hospitalized_with_symptoms","intensive_care","total_hospitalized","home_insulation"]
    district_data.print_details(features,actions)


if __name__ == '__main__':
    main([0,"C:\\Users\\daniel\\Desktop\\dpc-covid19-ita-regioni_sample.csv"])

