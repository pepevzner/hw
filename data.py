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


def create_filtered_dict(keys, zipped, feature, values, flag=True):
    feat_index = keys.index(feature)
    lst = [group for group in zipped if flag == (group[feat_index] in values)]
    unzipped = [list(t) for t in zip(*lst)]
    data = {k: v for k, v in zip(keys, unzipped)}
    return data


def filter_by_feature(data, feature, values):
    zipped = list(zip(*data.values()))
    keys = list(data.keys())
    return create_filtered_dict(keys, zipped, feature, values), \
        create_filtered_dict(keys, zipped, feature, values, False)


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
