import unittest
from CalorieCalculator import CalorieCalculator

class TestingUtils(unittest.TestCase):
    def setUp(self):
        self.calculator = CalorieCalculator()
        
    def test_calorie_intake_calculation(self):
        # Test case for calculating calorie intake
        food_items = [
            {"name": "Apple", "calories": 52},
            {"name": "Banana", "calories": 96},
            {"name": "Orange", "calories": 62}
        ]
        self.calculator.food_items = food_items
        total_calories = self.calculator.calculate_calorie_intake()
        self.assertEqual(total_calories, 210)

    def test_calorie_expenditure_calculation(self):
        # Test case for calculating calorie expenditure
        activities = [
            {"name": "Running", "calories": 350},
            {"name": "Cycling", "calories": 250},
            {"name": "Swimming", "calories": 400}
        ]
        self.calculator.activities = activities
        total_calories = self.calculator.calculate_calorie_expenditure()
        self.assertEqual(total_calories, 1000)

if __name__ == '__main__':
    unittest.main()
