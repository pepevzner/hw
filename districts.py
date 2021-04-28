import data


class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        self.dataset.set_districts_data([city for city in self.dataset.get_all_districts() if city[0] in letters])

    def print_details(self, features, statistic_functions):
        data.print_details(self.dataset.data,features,statistic_functions)

    def determine_day_type(self):
        pass

    def get_districts_class(self):
        districts_class={}
        for city,category in zip(self.dataset.get_all_districts(),self.dataset.data["type_day"]):
            districts_class[city]=category
        return districts_class
