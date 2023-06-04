from CalorieCalculator import CalorieCalculator
from UserInterface import CalorieTrackerUI
from FoodDatabase import FoodDatabase
from ReportGenerator import ReportGenerator
import datetime

def run_calorie_tracker():
    # Initialize the FoodDatabase, CalorieCalculator, and ReportGenerator
    food_database = FoodDatabase("food_database.db")
    calorie_calculator = CalorieCalculator(food_database)
    report_generator = ReportGenerator(food_database)

    # Generate a daily report for the current date
    current_date = datetime.date.today()
    daily_report = report_generator.generate_daily_report(current_date)
    print(daily_report)

    # Initialize the user interface
    ui = CalorieTrackerUI()
    ui.add_test_items()

    # Start the user interface event loop
    ui.root.mainloop()

if __name__ == "__main__":
    try:
        # Run the calorie tracker application
        run_calorie_tracker()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
