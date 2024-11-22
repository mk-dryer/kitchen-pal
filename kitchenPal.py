import tkinter as tk
from tkinter import messagebox
import random
import sqlite3


class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KitchenPal")
        self.root.geometry("400x400")

        # Initialize lists to track seen recipes, chosen recipes, and ingredients
        self.seen_recipes = []
        self.chosen_recipes = []
        self.ingredients = []
        self.current_recipe = None

        # Create welcome frame
        self.welcome_frame = tk.Frame(root)
        self.welcome_frame.pack(fill="both", expand=True)
        welcome_label = tk.Label(self.welcome_frame, text="Welcome to kitchen-pal.py!", font=("Arial", 16))
        welcome_label.pack(pady=20)
        proceed_button = tk.Button(self.welcome_frame, text="Proceed", command=self.proceed_to_main)
        proceed_button.pack(pady=10)

        # Create main frame
        self.main_frame = tk.Frame(root)

        # Suggest Recipe button
        suggest_button = tk.Button(self.main_frame, text="Suggest Recipe", command=self.suggest_recipe)
        suggest_button.pack(pady=10)

        # Recipe label to display suggestions
        self.recipe_label = tk.Label(self.main_frame, text="Your recipe will appear here.")
        self.recipe_label.pack(pady=10)

        # Confirm Recipe button
        confirm_button = tk.Button(
            self.main_frame,
            text="Confirm Recipe",
            command=self.confirm_recipe
        )
        confirm_button.pack(pady=10)

        # Listbox for chosen recipes
        self.menu_listbox = tk.Listbox(self.main_frame, height=6)
        self.menu_listbox.pack(pady=10)

        # Generate shopping list button
        shopping_list_button = tk.Button(self.main_frame, text="Generate Shopping List", command=self.generate_shopping_list)
        shopping_list_button.pack(pady=10)

    def proceed_to_main(self):
        self.welcome_frame.pack_forget()  # Hide welcome frame
        self.main_frame.pack(fill="both", expand=True)  # Show main frame

    def suggest_recipe(self):
        conn = sqlite3.connect('recipeCodex.db')  # Connect to the database
        cursor = conn.cursor()
        cursor.execute("SELECT RecipeName, RecipeIngredients FROM recipes")  # Fetch all recipes
        all_recipes = cursor.fetchall()
        conn.close()

        unseen_recipes = [recipe for recipe in all_recipes if recipe[0] not in [r[0] for r in self.seen_recipes]]

        if unseen_recipes:  # If there are unseen recipes
            self.current_recipe = random.choice(unseen_recipes)  # Pick one at random
            self.seen_recipes.append(self.current_recipe)  # Mark it as seen
            self.recipe_label.config(text=f"How about: {self.current_recipe[0]}?")
        else:
            self.recipe_label.config(text="You've seen all the recipes.")
            self.current_recipe = None  # No recipe available to confirm

    def confirm_recipe(self):
        if self.current_recipe:  # If a recipe is currently suggested
            # Add the current recipe's ingredients and name to respective lists
            self.ingredients.append(self.current_recipe[1])
            self.menu_listbox.insert(tk.END, self.current_recipe[0])
            self.recipe_label.config(text="Recipe added! Suggest another recipe.")  # Feedback
            self.current_recipe = None  # Reset current recipe
        else:
            messagebox.showinfo("No Recipe Selected", "Please suggest a recipe first.")

    def generate_shopping_list(self):
        # Generate and display the shopping list
        shopping_list = []
        for ingredient in self.ingredients:  # Split ingredients by commas
            shopping_list.extend([i.strip() for i in ingredient.split(",")])  # Add to the list
        shopping_list = sorted(set(shopping_list))  # Deduplicate and sort the list
        messagebox.showinfo("Shopping List", "\n".join(shopping_list))  # Display the list


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()