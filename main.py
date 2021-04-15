import sys
import data
import statistics


def main(argv):
    features = argv[2].split(", ")
    print(features)
    info = data.load_data(argv[1], features)
    data.filter_by_feature(info,"season",{0,1})


if __name__ == '__main__':
    main([0, "C:\\Users\\daniel\\Desktop\\london_sample.csv", "hum, t1, cnt, season, is_holiday"])
    #temporary for tests
    #main(sys.argv)