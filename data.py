import pandas


def load_data(path, features):
    """
    returns filtered information from database in dictionary form
    :param path: path of the database file
    :param features: wanted features for analysis
    :return: dict with wanted features and corresponding values
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    filtered = {d: data[d] for d in features}
    return filtered


def filter_by_feature(data, feature, values):
    list(zip(*data.values()))

    pass


def print_details(data, features, statistic_functions):
    """
    prints information about given features from the dataset, according to given functions
    :param data: dataset to print info about
    :param features: wanted features
    :param statistic_functions: functions for the dataset
    :return: void
    """
    for category in features:
        print(category + ": " + ', '.join([str(func(data[category])) for func in statistic_functions]))
