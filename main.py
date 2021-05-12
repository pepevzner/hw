import data
import statistics
import districts
import sys


def main(argv):
    covid_data = data.Data(argv[1])
    district_data = districts.Districts(covid_data)
    district_data.filter_districts(["L", "S"])

    print("Question 1:")
    actions = [statistics.mean, statistics.median]
    features = ["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"]
    district_data.print_details(features, actions)

    print("\nQuestion 2:")
    covid_data = data.Data(argv[1])
    district_data = districts.Districts(covid_data)
    district_data.determine_day_type()
    status = district_data.get_districts_class()
    print(f"Number of districts: {len(status.keys())}")
    non_green_amount = len(status.keys()) - sum(list(status.values()))
    print(f"Number of not green districts: {non_green_amount}")
    print("Will a lockdown be forced on whole of Italy?: " + ("No" if non_green_amount <= 10 else "Yes"))


if __name__ == '__main__':
    main(sys.argv)
