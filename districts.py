import data


class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        self.dataset.set_districts_data([city for city in self.dataset.get_all_districts() if city[0] in letters])

    def print_details(self, features, statistic_functions):
        data.print_details(self.dataset.data, features, statistic_functions)

    def determine_day_type(self):
        day_data = []
        for new, healed in zip(self.dataset.data["new_positives"], self.dataset.data["resigned_healed"]):
            day_data.append(1 if (new < healed) else 0)

        self.dataset.data["day_type"] = day_data

    def get_districts_class(self):
        districts_class = {}
        for district, day_type in zip(self.dataset.data["denominazione_region"], self.dataset.data["day_type"]):
            if district not in districts_class:
                districts_class[district] = 0
            districts_class[district] += day_type
        for district, green_day_amount in districts_class.items():
            districts_class[district] = 1 if green_day_amount > 340 else 0
        return districts_class
