import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to suggest a recipe from the database
def suggest_recipe():
    # Connect to the SQLite database
    conn = sqlite3.connect('recipeCodex.db')
    cursor = conn.cursor()

    # Query to select a random recipe
    cursor.execute("SELECT RecipeName FROM recipes ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    conn.close()

    if result:
        recipe_label.config(text=f"How about: {result[0]}?")
    else:
        recipe_label.config(text="No recipes found!")

# Function to confirm and add the recipe to the weekly list
def confirm_recipe():
    selected_recipe = recipe_label.cget("text").replace("How about: ", "").rstrip("?")
    if selected_recipe:
        weekly_listbox.insert(tk.END, selected_recipe)
    else:
        messagebox.showerror("Error", "No recipe selected")

# Function to generate the shopping list
def generate_shopping_list():
    messagebox.showinfo("Shopping List", "This will generate your shopping list.")

# Function to hide welcome screen and display main interface
def proceed_to_main():
    welcome_frame.pack_forget()  # Hide the welcome frame
    main_frame.pack(fill="both", expand=True)  # Show the main frame

# Create the main window
root = tk.Tk()
root.title("KitchenPal")
root.geometry("400x400")

# Welcome Frame
welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(welcome_frame, text="Welcome to kitchen-pal.py!", font=("Arial", 16))
welcome_label.pack(pady=20)

proceed_button = tk.Button(welcome_frame, text="Proceed", command=proceed_to_main)
proceed_button.pack(pady=10)

# Main Frame (Initially hidden)
main_frame = tk.Frame(root)

# Suggest Recipe Button
suggest_button = tk.Button(main_frame, text="Suggest Recipe", command=suggest_recipe)
suggest_button.pack(pady=10)

# Label to display suggested recipe
recipe_label = tk.Label(main_frame, text="Your recipe suggestion will appear here.")
recipe_label.pack(pady=10)

# Confirm Button to add recipe to weekly list
confirm_button = tk.Button(main_frame, text="Confirm Recipe", command=confirm_recipe)
confirm_button.pack(pady=10)

# Listbox to display the weekly list
weekly_listbox = tk.Listbox(main_frame, height=6)
weekly_listbox.pack(pady=10)

# Button to generate shopping list
shopping_list_button = tk.Button(main_frame, text="Generate Shopping List", command=generate_shopping_list)
shopping_list_button.pack(pady=10)

# Run the main loop
root.mainloop()


# # TODO: locate .db to check file architecture 

# # import libs and functions 

# import os
# import random
# import sqlite3
# import tkinter as tk

# # verify database and program located in same folder

# def locate_db():
#     cwd = os.getcwd()
#     filepath = os.path.join(cwd, "recipeCodex.db")
#     if os.path.exists(filepath):
#         print("I've located your recipe codex.")
#     else:
#         print("Uh-oh! I can't find", filepath + ". Make sure that I'm stored in the same folder as", filepath+".")
#         exit()


# # connect to database 

# conn = sqlite3.connect(r".\recipeCodex.db") 
# cursor = conn.cursor()


# # initialize an empty list to store selected & declined recipes

# selected_recipes = []
# declined_recipes = []


# # function to propose recipes 
# def propose_recipe():
#     cursor.execute("SELECT RecipeName, RecipeIngredients, RecipeLink FROM recipes ORDER BY RANDOM()")
#     rows = cursor.fetchall()
#     conn.close()
#     known_recipes = [{'RecipeName': row[0], 'RecipeIngredients': row[1]} for row in rows] # process all recipe name & ingredients as dict 
#     available_recipes = [recipe for recipe in known_recipes if recipe not in selected_recipes and recipe not in declined_recipes] # available recipes = all known recipes not yet selected or declined
#     recipe = random.choice(available_recipes) # randomly select from list of available recipes 
#     recipe_label.config(text=f"Do you want to make {recipe}?")
#     # else:
#     #     recipe_label.config(text="No recipes found!")

#     # global done # declare var done 
#     # cursor.execute("SELECT RecipeName, RecipeIngredients FROM recipes") # select name & ingredients cols from recipe entries 
#     # rows = cursor.fetchall() # fetch all rows    
#     # while not done: # while done = False: 
#     #     known_recipes = [{'RecipeName': row[0], 'RecipeIngredients': row[1]} for row in rows] # process all recipe name & ingredients as dict 
#     #     available_recipes = [recipe for recipe in known_recipes if recipe not in selected_recipes and recipe not in declined_recipes] # available recipes = all known recipes not yet selected or declined 
#     #     if not available_recipes: # if no recipes available: 
#     #         print("You've already selected all available recipes.")
#     #         done = True
#     #         break
#     #     recipe = random.choice(available_recipes) # randomly select from list of available recipes 
#     #     print(f"Do you want to make {recipe['RecipeName']}? (y/n)") # propose recipe to user 
#     #     choice = input().strip().lower() # process input 
#     #     if choice == 'y':
#     #         selected_recipes.append(recipe) # append to selected list 
#     #         print(f"{recipe['RecipeName']} added to your list.") 
#     #     else: 
#     #         declined_recipes.append(recipe) # append to declined 
#     #         print("No problem.") # and proceed to next choice 
#     #     another_choice = input("Do you want to choose another recipe? (y/n) ").strip().lower()
#     #     if another_choice != 'y':
#     #         gen_list = input("Are you ready to generate your shopping list? (y/n) ").strip().lower()
#     #         if gen_list == "y":
#     #             done = True
#     #             break


# # function to generate a shopping list
# def generate_shopping_list(): 
#     shopping_list = [] # intialize empty shopping list 
#     for recipe in selected_recipes: # for each recipe 
#         ingredients = recipe['RecipeIngredients'] # access ingredients 
#         for ingredient in ingredients.split(","): # split by comma  
#             shopping_list.append(ingredient.strip()) # and append to shopping list 
#     shopping_list = sorted(list(set(shopping_list))) # remove duplicates and sort the shopping list
#     return shopping_list

# def proceed_to_main():
#     welcome_frame.pack_forget()  # Hide the welcome frame
#     main_frame.pack(fill="both", expand=True)  # Show the main frame

# # main program

# root = tk.Tk()
# root.title("KitchenPal")
# root.geometry("400x400")

# # welcome frame
# welcome_frame = tk.Frame(root)
# welcome_frame.pack(fill="both", expand=True)

# welcome_label = tk.Label(welcome_frame, text="Welcome to kitchen-pal.py!", font=("Arial", 16))
# welcome_label.pack(pady=20)

# proceed_button = tk.Button(welcome_frame, text="Proceed", command=proceed_to_main)
# proceed_button.pack(pady=10)

# main_frame = tk.Frame(root)
# suggest_button = tk.Button(main_frame, text="Suggest Recipe", command=propose_recipe)
# suggest_button.pack(pady=10)

# recipe_label = tk.Label(main_frame, text="Your recipe suggestion will appear here.")
# recipe_label.pack(pady=10)

# root.mainloop()

# print("Welcome to kitchen-pal!")
# locate_db()
# done = False # declare done as False to trigger loop 
# propose_recipe() # invoke propose recipe 
# if done: # once done = True: 
#     print("Great! You've selected the following recipes:") # review selected recipes 
#     for recipe in selected_recipes:
#         print(recipe['RecipeName'])
#     shopping_list = generate_shopping_list() # invoke generate list
#     print("\nHere's your shopping list:")
#     for item in shopping_list:
#         print(item)
# else:
#     print("You haven't selected any recipes. Have a great day!")

# conn.close()

