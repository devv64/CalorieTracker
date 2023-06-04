from tkinter import Tk, Label, Button, Entry, messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.express as px
from CalorieCalculator import CalorieCalculator
from FoodDatabase import FoodDatabase

class CalorieTrackerUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calorie Tracker App")
        food_database = FoodDatabase("food_database.db")
        self.calorie_calculator = CalorieCalculator(food_database)

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Welcome to the Calorie Tracker App!", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)

        food_frame = ttk.LabelFrame(self.root, text="Add Food Item", padding=20)
        food_frame.pack(pady=10)

        self.food_name_label = Label(food_frame, text="Food Item:", font=("Arial", 12))
        self.food_name_label.grid(row=0, column=0, sticky="w")

        self.food_name_entry = Entry(food_frame, font=("Arial", 12))
        self.food_name_entry.grid(row=0, column=1, padx=10)

        self.food_calories_label = Label(food_frame, text="Calories:", font=("Arial", 12))
        self.food_calories_label.grid(row=1, column=0, sticky="w")

        self.food_calories_entry = Entry(food_frame, font=("Arial", 12))
        self.food_calories_entry.grid(row=1, column=1, padx=10)

        self.add_food_button = Button(food_frame, text="Add Food Item", command=self.add_food_item, font=("Arial", 12, "bold"))
        self.add_food_button.grid(row=2, columnspan=2, pady=10)

        activity_frame = ttk.LabelFrame(self.root, text="Add Activity", padding=20)
        activity_frame.pack(pady=10)

        self.activity_name_label = Label(activity_frame, text="Activity:", font=("Arial", 12))
        self.activity_name_label.grid(row=0, column=0, sticky="w")

        self.activity_name_entry = Entry(activity_frame, font=("Arial", 12))
        self.activity_name_entry.grid(row=0, column=1, padx=10)

        self.activity_calories_label = Label(activity_frame, text="Calories:", font=("Arial", 12))
        self.activity_calories_label.grid(row=1, column=0, sticky="w")

        self.activity_calories_entry = Entry(activity_frame, font=("Arial", 12))
        self.activity_calories_entry.grid(row=1, column=1, padx=10)

        self.add_activity_button = Button(activity_frame, text="Add Activity", command=self.add_activity, font=("Arial", 12, "bold"))
        self.add_activity_button.grid(row=2, columnspan=2, pady=10)

        search_frame = ttk.LabelFrame(self.root, text="Search and Display", padding=20)
        search_frame.pack(pady=10)

        self.search_button = Button(search_frame, text="Search Food Item", command=self.search_food_item, font=("Arial", 12, "bold"))
        self.search_button.grid(row=0, column=0, padx=10, pady=5)

        self.display_food_button = Button(search_frame, text="Display All Food Items", command=self.display_all_food_items, font=("Arial", 12, "bold"))
        self.display_food_button.grid(row=0, column=1, padx=10, pady=5)

        self.display_activity_button = Button(search_frame, text="Display All Activities", command=self.display_all_activities, font=("Arial", 12, "bold"))
        self.display_activity_button.grid(row=0, column=2, padx=10, pady=5)

        visualize_frame = ttk.LabelFrame(self.root, text="Visualize Data", padding=20)
        visualize_frame.pack(pady=10)

        self.visualize_intake_button = Button(visualize_frame, text="Visualize Calorie Intake", command=self.visualize_calorie_intake, font=("Arial", 12, "bold"))
        self.visualize_intake_button.grid(row=0, column=0, padx=10, pady=5)

        self.visualize_expenditure_button = Button(visualize_frame, text="Visualize Calorie Expenditure", command=self.visualize_calorie_expenditure, font=("Arial", 12, "bold"))
        self.visualize_expenditure_button.grid(row=0, column=1, padx=10, pady=5)

        self.exit_button = Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12))
        self.exit_button.pack(pady=20)

    def add_food_item(self):
        name = self.food_name_entry.get()
        calories = self.food_calories_entry.get()

        if name and calories:
            self.calorie_calculator.add_food_item(name, int(calories))
            messagebox.showinfo("Success", "Food item added.")
            self.food_name_entry.delete(0, 'end')
            self.food_calories_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Please enter both name and calories.")

    def search_food_item(self):
        keyword = self.food_name_entry.get()

        if keyword:
            results = self.calorie_calculator.search_food_item(keyword)
            if results:
                messagebox.showinfo("Search Results", "\n".join(results))
            else:
                messagebox.showinfo("Search Results", "No matching food items found.")
        else:
            messagebox.showerror("Error", "Please enter a keyword.")

    def display_all_food_items(self):
        results = self.calorie_calculator.display_all_food_items()
        if results:
            messagebox.showinfo("All Food Items", "\n".join(results))
        else:
            messagebox.showinfo("All Food Items", "No food items in the database.")

    def add_activity(self):
        name = self.activity_name_entry.get()
        calories = self.activity_calories_entry.get()

        if name and calories:
            self.calorie_calculator.add_activity(name, int(calories))
            messagebox.showinfo("Success", "Activity added.")
            self.activity_name_entry.delete(0, 'end')
            self.activity_calories_entry.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Please enter both name and calories for the activity.")

    def display_all_activities(self):
        results = self.calorie_calculator.display_all_activities()
        if results:
            messagebox.showinfo("All Activities", "\n".join(results))
        else:
            messagebox.showinfo("All Activities", "No activities in the database.")

    def visualize_calorie_intake(self):
        food_items = self.calorie_calculator.food_items
        if food_items:
            names = [item["name"] for item in food_items]
            calories = [item["calories"] for item in food_items]

            # Create a donut chart
            fig = go.Figure(data=[go.Pie(labels=names, values=calories, hole=0.4)])
            fig.update_traces(textinfo='percent+label')
            fig.update_layout(title="Calorie Intake")

            # Customize the layout and style
            fig.update_layout(
                font_family="Arial",
                plot_bgcolor="white",
                showlegend=False
            )

            # Render the graph
            pio.show(fig)
        else:
            messagebox.showinfo("No Data", "No food items available.")

    def visualize_calorie_expenditure(self):
        activities = self.calorie_calculator.activities
        if activities:
            names = [activity["name"] for activity in activities]
            calories = [activity["calories"] for activity in activities]

            # Create a sunburst chart
            fig = go.Figure(go.Sunburst(
                labels=names,
                parents=['' for _ in names],
                values=calories,
                branchvalues="total",
                hovertemplate='<b>%{label}</b><br>Calories: %{value}<extra></extra>',
                marker=dict(colors=px.colors.qualitative.Plotly)
            ))
            fig.update_layout(title="Calorie Expenditure")

            # Customize the layout and style
            fig.update_layout(
                font_family="Arial",
                plot_bgcolor="white",
                showlegend=False
            )

            # Render the graph
            pio.show(fig)
        else:
            messagebox.showinfo("No Data", "No activities available.")

    def add_test_items(self):
        # Add sample food items
        self.calorie_calculator.add_food_item("Apple", 52)
        self.calorie_calculator.add_food_item("Chicken Breast", 165)
        self.calorie_calculator.add_food_item("Pasta", 131)
        self.calorie_calculator.add_food_item("Salad", 25)

        # Add sample activity items
        self.calorie_calculator.add_activity("Running", 350)
        self.calorie_calculator.add_activity("Cycling", 250)
        self.calorie_calculator.add_activity("Swimming", 400)
        self.calorie_calculator.add_activity("Yoga", 150)

        messagebox.showinfo("Test Items Added", "Sample food and activity items have been added.")

    def run(self):
        self.root.mainloop()

# Testing:
# ui = CalorieTrackerUI()
# ui.add_test_items()
# ui.run()
