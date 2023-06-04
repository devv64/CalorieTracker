class CalorieCalculator:
    def __init__(self, food_database):
        self.food_database = food_database
        self.food_items = []
        self.activities = []

    def add_food_item(self, name, calories):
        self.food_database.add_food_item(name, calories)
        self.food_items.append({"name": name, "calories": calories})

    def search_food_item(self, keyword):
        return self.food_database.search_food_item(keyword)

    def display_all_food_items(self):
        return self.food_database.display_all_food_items()

    def add_activity(self, name, calories):
        self.activities.append({"name": name, "calories": calories})

    def search_activity(self, keyword):
        results = [activity["name"] for activity in self.activities if keyword.lower() in activity["name"].lower()]
        return results

    def display_all_activities(self):
        results = [f"{activity['name']}: {activity['calories']} calories" for activity in self.activities]
        return results

    def calculate_calorie_intake(self):
        food_items = self.food_database.get_all_food_items()
        total_calories = sum(item["calories"] for item in food_items)
        return total_calories

    def calculate_calorie_expenditure(self):
        total_calories = sum(activity["calories"] for activity in self.activities)
        return total_calories

    def calculate_net_calories(self):
        calorie_intake = self.calculate_calorie_intake()
        calorie_expenditure = self.calculate_calorie_expenditure()
        net_calories = calorie_intake - calorie_expenditure
        return net_calories
