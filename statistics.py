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
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def median(values):
    """
    gets median
    :param values: given iterable
    :return: median of iterable
    """
    length = len(values)
    if length == 0:
        return 0
    ordered = sorted(values)
    if length % 2 == 0:
        return (ordered[int(length / 2) - 1] + ordered[int(length / 2)]) / 2
    else:
        return ordered[ceil(length / 2) - 1]


def population_statistics(feature_description, data, treatment, target, threshold, is_above,
                          statistic_functions):
    population = [v for v, treat_val in zip(data[target], data[treatment]) if ((treat_val > threshold) == is_above)]
    print(f"{feature_description} \n{treatment}: {', '.join([str(func(population)) for func in statistic_functions])}")
