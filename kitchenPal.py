import tkinter as tk
from tkinter import messagebox
import random
import sqlite3

# initialize an empty list to store selected & declined recipes

seen_recipes = []

# suggest a recipe from the database
def suggest_recipe():
    global selected_recipes  # access global list  

    conn = sqlite3.connect('recipeCodex.db') # connect to db
    cursor = conn.cursor()

    cursor.execute("SELECT RecipeName, RecipeIngredients FROM recipes") # select all recipes
    all_recipes = cursor.fetchall() # fetch all as tuples
    conn.close()


    unseen_recipes = [recipe for recipe in all_recipes if recipe[0] not in [r[0] for r in seen_recipes]]
    
    if unseen_recipes: # if the unselected_recipes list is populated: 
        recipe = random.choice(unseen_recipes) # select one at random
        seen_recipes.append(recipe)  # append it to the list of seen recipes
        recipe_label.config(text=f"How about: {recipe[0]}?")
    else:
        recipe_label.config(text="No recipes found!")

# add recipe to listbox
def confirm_recipe():
    recipe_item = recipe_label.cget("text").replace("How about: ", "").rstrip("?") # format label for listbox  
    menu_listbox.insert(tk.END, recipe_item) # insert formatted label into listbox

# generate the shopping list when triggered 
def generate_shopping_list():
    messagebox.showinfo("Shopping List", "This will generate your shopping list.")

# hide welcome screen and display to main interface when triggered
def proceed_to_main():
    welcome_frame.pack_forget()  # hide welcome frame
    main_frame.pack(fill="both", expand=True)  # show main frame

# create main window
root = tk.Tk()
root.title("KitchenPal")
root.geometry("400x400")

# create welcome frame
welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="both", expand=True)
welcome_label = tk.Label(welcome_frame, text="Welcome to kitchen-pal.py!", font=("Arial", 16))
welcome_label.pack(pady=20)
proceed_button = tk.Button(welcome_frame, text="Proceed", command=proceed_to_main)
proceed_button.pack(pady=10)

# create main frame with Suggest button, recipe label, Confirm button, listbox
main_frame = tk.Frame(root)
suggest_button = tk.Button(main_frame, text="Suggest Recipe", command=suggest_recipe)
suggest_button.pack(pady=10)
recipe_label = tk.Label(main_frame, text="Your recipe will appear here.")
recipe_label.pack(pady=10)
confirm_button = tk.Button(main_frame, text="Confirm Recipe", command=confirm_recipe)
confirm_button.pack(pady=10)
menu_listbox = tk.Listbox(main_frame, height=6)
menu_listbox.pack(pady=10)

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

