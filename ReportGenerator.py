class ReportGenerator:
    def __init__(self, food_database):
        self.food_database = food_database

    def generate_daily_report(self, date):
        food_items = self.get_food_items(date)
        total_calories = self.calculate_total_calories(food_items)
        report = self.format_report(date, food_items, total_calories)
        return report

    def get_food_items(self, date):
        # Retrieve all food items logged for the given date from the database
        food_items = self.food_database.get_food_items_by_date(date)
        return food_items

    def calculate_total_calories(self, food_items):
        total_calories = sum(item[1] for item in food_items)
        return total_calories

    def format_report(self, date, food_items, total_calories):
        report = f"Daily Report - {date}\n\n"
        report += "Food Items:\n"
        for item in food_items:
            report += f"- {item[0]}: {item[1]} calories\n"
        report += f"\nTotal Calories: {total_calories}"
        return report
