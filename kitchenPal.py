# TODO: locate .db to check file architecture 

# import libs and functions 

import os
import random
import sqlite3
import tkinter as tk

# verify database and program located in same folder

def locate_db():
    cwd = os.getcwd()
    filepath = os.path.join(cwd, "recipeCodex.db")
    if os.path.exists(filepath):
        print("I've located your recipe codex.")
    else:
        print("Uh-oh! I can't find", filepath + ". Make sure that I'm stored in the same folder as", filepath+".")
        exit()


# connect to database 

conn = sqlite3.connect(r".\recipeCodex.db") 
cursor = conn.cursor()


# initialize an empty list to store selected & declined recipes

selected_recipes = []
declined_recipes = []


# function to propose recipes 
def propose_recipe():
    global done # declare var done 
    cursor.execute("SELECT RecipeName, RecipeIngredients FROM recipes") # select name & ingredients cols from recipe entries 
    rows = cursor.fetchall() # fetch all rows    
    while not done: # while done = False: 
        known_recipes = [{'RecipeName': row[0], 'RecipeIngredients': row[1]} for row in rows] # process all recipe name & ingredients as dict 
        available_recipes = [recipe for recipe in known_recipes if recipe not in selected_recipes and recipe not in declined_recipes] # available recipes = all known recipes not yet selected or declined 
        if not available_recipes: # if no recipes available: 
            print("You've already selected all available recipes.")
            done = True
            break
        recipe = random.choice(available_recipes) # randomly select from list of available recipes 
        print(f"Do you want to make {recipe['RecipeName']}? (y/n)") # propose recipe to user 
        choice = input().strip().lower() # process input 
        if choice == 'y':
            selected_recipes.append(recipe) # append to selected list 
            print(f"{recipe['RecipeName']} added to your list.") 
        else: 
            declined_recipes.append(recipe) # append to declined 
            print("No problem.") # and proceed to next choice 
        another_choice = input("Do you want to choose another recipe? (y/n) ").strip().lower()
        if another_choice != 'y':
            gen_list = input("Are you ready to generate your shopping list? (y/n) ").strip().lower()
            if gen_list == "y":
                done = True
                break


# function to generate a shopping list
def generate_shopping_list(): 
    shopping_list = [] # intialize empty shopping list 
    for recipe in selected_recipes: # for each recipe 
        ingredients = recipe['RecipeIngredients'] # access ingredients 
        for ingredient in ingredients.split(","): # split by comma  
            shopping_list.append(ingredient.strip()) # and append to shopping list 
    shopping_list = sorted(list(set(shopping_list))) # remove duplicates and sort the shopping list
    return shopping_list

# main program

root = tk.Tk()
root.title("KitchenPal")
root.geometry("400x400")

# Welcome Frame
welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(welcome_frame, text="Welcome to kitchen-pal.py!", font=("Arial", 16))
welcome_label.pack(pady=20)
root.mainloop()

print("Welcome to kitchen-pal!")
locate_db()
done = False # declare done as False to trigger loop 
propose_recipe() # invoke propose recipe 
if done: # once done = True: 
    print("Great! You've selected the following recipes:") # review selected recipes 
    for recipe in selected_recipes:
        print(recipe['RecipeName'])
    shopping_list = generate_shopping_list() # invoke generate list
    print("\nHere's your shopping list:")
    for item in shopping_list:
        print(item)
else:
    print("You haven't selected any recipes. Have a great day!")

conn.close()

