import data


class Districts:
    def __init__(self, dataset):
        """
        initializes class with with the Data class
        :param dataset: the instance of data
        """
        self.dataset = dataset

    def filter_districts(self, letters):
        """
        filters districts by their first letter
        :param letters:the letters to filter by
        """
        self.dataset.set_districts_data([city for city in self.dataset.get_all_districts() if city[0] in letters])

    def print_details(self, features, statistic_functions):
        """
        prints the statistic details of the requested features
        :param features:the features to print details
        :param statistic_functions:the functions to get the information about the features
        """
        data.print_details(self.dataset.data, features, statistic_functions)

    def determine_day_type(self):
        """
        adds new feature new_day to dataset 1 for a good day 0 otherwise
        """
        day_data = []
        for new, healed in zip(self.dataset.data["new_positives"], self.dataset.data["resigned_healed"]):
            day_data.append(1 if (new < healed) else 0)

        self.dataset.data["day_type"] = day_data

    def get_districts_class(self):
        """
        creates creates a dictionary of districts and determines if they are considered green
        :return: dictionary of districts:status
        """
        districts_class = dict.fromkeys(self.dataset.get_all_districts(), 0)
        for district, day_type in zip(self.dataset.data["denominazione_region"], self.dataset.data["day_type"]):
            districts_class[district] += day_type
        for district, green_day_amount in districts_class.items():
            districts_class[district] = 1 if green_day_amount > 340 else 0
        return districts_class
