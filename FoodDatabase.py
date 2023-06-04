import sqlite3

class FoodDatabase:
    def __init__(self, database_file):
        self.database_file = database_file
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        # Create the food_items table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS food_items (
                id INTEGER PRIMARY KEY,
                name TEXT,
                calories INTEGER,
                date DATE
            )
        """)

        conn.commit()
        conn.close()

    def add_food_item(self, name, calories):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        # Insert the food item into the database with the current date
        cursor.execute("""
            INSERT INTO food_items (name, calories, date)
            VALUES (?, ?, DATE('now'))
        """, (name, calories))

        conn.commit()
        conn.close()

    def search_food_item(self, keyword):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        # Search for food items matching the keyword
        cursor.execute("""
            SELECT name
            FROM food_items
            WHERE name LIKE ?
        """, ('%' + keyword + '%',))

        results = cursor.fetchall()
        conn.close()

        if results:
            print("Search results:")
            for result in results:
                print("- " + result[0])
        else:
            print("No matching food items found.")

    def display_all_food_items(self):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        # Retrieve all food items from the database
        cursor.execute("""
            SELECT name
            FROM food_items
        """)

        results = cursor.fetchall()
        conn.close()

        if results:
            print("All food items in the database:")
            for result in results:
                print("- " + result[0])
        else:
            print("No food items in the database.")

    def get_food_items_by_date(self, date):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        # Retrieve food items for the given date
        cursor.execute("""
            SELECT name, calories
            FROM food_items
            WHERE date = ?
        """, (date,))

        results = cursor.fetchall()
        conn.close()

        return results
