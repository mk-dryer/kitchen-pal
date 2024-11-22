import tkinter as tk # for GUI 
from tkinter import messagebox # for pop-ups 
import random # for random choices 
import sqlite3 # for connenting to db 


class RecipeApp:
    def __init__(self, root):
        
        # root window setup 
        self.root = root 
        self.root.title("KitchenPal")
        self.root.geometry("400x400")

        # welcome frame setup
        self.welcome_frame = tk.Frame(root)
        self.welcome_frame.pack(fill="both", expand=True)
        welcome_label = tk.Label(self.welcome_frame, text="Welcome to kitchen-pal.py!", font=("Arial", 16))
        welcome_label.pack(pady=20)
        proceed_button = tk.Button(self.welcome_frame, text="Proceed", command=self.proceed_to_main) # proceed to main frame when selected
        proceed_button.pack(pady=10)

        # initialize empty lists to track recipes seen by the user and recipes chosen by the user
        self.chosen_recipes = []
        self.ingredients = [] 
        self.current_recipe = None
        self.seen_recipes = []

        # main frame setup
        self.main_frame = tk.Frame(root)

        # suggest recipe button
        suggest_button = tk.Button(self.main_frame, text="Suggest Recipe", command=self.suggest_recipe)  
        suggest_button.pack(pady=10)

        # suggested recipe label
        self.recipe_label = tk.Label(self.main_frame, text="Your recipe will appear here.")
        self.recipe_label.pack(pady=10)

        # confirm recipe button
        confirm_button = tk.Button(
            self.main_frame,
            text="Confirm Recipe",
            command=self.confirm_recipe
        )
        confirm_button.pack(pady=10)

        # Listbox to track chosen recipes
        self.menu_listbox = tk.Listbox(self.main_frame, height=6)
        self.menu_listbox.pack(pady=10)

        # generate shopping list button
        shopping_list_button = tk.Button(self.main_frame, text="Generate Shopping List", command=self.generate_shopping_list)
        shopping_list_button.pack(pady=10)

    def proceed_to_main(self):
        self.welcome_frame.pack_forget()  # hide welcome frame
        self.main_frame.pack(fill="both", expand=True)  # show main frame

    def suggest_recipe(self):
        conn = sqlite3.connect('recipeCodex.db')  # connect to the database
        cursor = conn.cursor()
        cursor.execute("SELECT RecipeName, RecipeIngredients FROM recipes")  # fetch all recipes
        all_recipes = cursor.fetchall()
        conn.close()

        unseen_recipes = [recipe for recipe in all_recipes if recipe[0] not in [r[0] for r in self.seen_recipes]]

        if unseen_recipes:  # if there are unseen recipes: 
            self.current_recipe = random.choice(unseen_recipes)  # pick recipe at random
            self.seen_recipes.append(self.current_recipe)  # mark recipe as seen
            self.recipe_label.config(text=f"How about: {self.current_recipe[0]}?") # suggest recipe to user
        else:
            self.recipe_label.config(text="You've seen all the recipes.")
            self.current_recipe = None

    def confirm_recipe(self):
        if self.current_recipe:  # if a recipe is selected: 
            self.ingredients.append(self.current_recipe[1]) #  append ingredients to ingredients list 
            self.menu_listbox.insert(tk.END, self.current_recipe[0]) # insert name into listbox 
            self.recipe_label.config(text="Recipe added! Suggest another recipe?")  # confirm selection 
            self.current_recipe = None  # reset
        else:
            messagebox.showinfo("Uh-oh!", "Please suggest a recipe first.") # throw an error if user selects confirm while no recipe is suggested 

    def generate_shopping_list(self):
        shopping_list = [] # intialize empty shopping list 
        for ingredient in self.ingredients:  # split ingredients by commas (ingredients are stored in the table as a comma-separated list)
            shopping_list.extend([i.strip() for i in ingredient.split(",")])  # add ingredients to list
        shopping_list = sorted(set(shopping_list))  # deduplicate and sort the list
        messagebox.showinfo("Shopping List", "\n".join(shopping_list))  # display the list as message box 


# run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
