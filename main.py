import sys
import data
import statistics


def main(argv):
    features = argv[2].split(", ")
    print(features)
    info = data.load_data(argv[1], features)

    # question 1
    print("Question 1:")
    features = ["hum", "t1", "cnt"]
    actions = [statistics.sum, statistics.mean, statistics.median]
    summer = data.filter_by_feature(info, "season", {1})[0]
    holiday = data.filter_by_feature(info, "is_holiday", {1})[0]
    print("Summer:")
    data.print_details(summer, features, actions)
    print("Holiday:")
    data.print_details(holiday, features, actions)
    print("All:")
    data.print_details(info, features, actions)

    # question 2
    print("\nQuestion 2:")
    T1 = 13.0
    actions = [statistics.mean, statistics.median]
    winter = data.filter_by_feature(info, "season", {3})[0]
    winter_holiday, winter_weekday = data.filter_by_feature(winter, "is_holiday", {1})
    for above in [False, True]:
        print(f"If t1{'>' if above else '<='}13.0, then:")
        statistics.population_statistics("Winter holiday records:", winter_holiday, "t1", "cnt", T1, above, actions)
        statistics.population_statistics("Winter weekday records:", winter_weekday, "t1", "cnt", T1, above, actions)


if __name__ == '__main__':
    main([0, "C:\\Users\\daniel\\Desktop\\london_sample.csv", "hum, t1, cnt, season, is_holiday"])
    # temporary for tests
    # main(sys.argv)
