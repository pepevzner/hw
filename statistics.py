from math import ceil


def sum(values):
    """
    calculates sum
    :param values: iterable
    :return: the sum
    """
    s = 0
    for i in values:
        s += i
    return s


def mean(values):
    """
    calculates average
    :param values: given iterable
    :return: mean average of iterable
    """
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def median(values):
    """
    calculates median
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
    """
    creates the list of target for the treatment population and prints given statistics
    :param feature_description: description of the printed stats
    :param data:dataset
    :param treatment:which feature to filter by
    :param target:which feature of the needed population to analyze
    :param threshold:threshold of the treatment feature
    :param is_above:take treatment values greater then threshold or equal/lower then if false
    :param statistic_functions:which statistics to print
    """
    population = [v for v, treat_val in zip(data[target], data[treatment]) if ((treat_val > threshold) == is_above)]
    print(f"{feature_description} \n{treatment}: {', '.join([str(func(population)) for func in statistic_functions])}")
