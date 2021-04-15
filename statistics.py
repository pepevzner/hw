from math import ceil


def sum(values):
    """
    sums given iterable
    :param values: iterable
    :return: the sum
    """
    s = 0
    for i in values:
        s += i
    return s


def mean(values):
    """
    returns average
    :param values: given iterable
    :return: mean average of iterable
    """
    return sum(values) / len(values)


def median(values):
    """
    gets median
    :param values: given iterable
    :return: median of iterable
    """
    length = len(values)
    sorted_vals = sorted(values)
    result = sorted_vals[ceil(length / 2)]
    if (length % 2 == 0):
        result = (result + sorted_vals[length / 2 + 1]) / 2
    return result


def population_statistics(feature_description, data, treatment, target, threshold, is_above,
                          statistic_functions):
    pass
