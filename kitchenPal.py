# TODO: update references to table column names

# import libs and functions 

import os
import random
import sqlite3

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

# create a table to store recipes if not already exists 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         Recipe_Name TEXT,
         Recipe_Ingredients TEXT, 
         Recipe_Link TEXT
     )
 """)
conn.commit()


# initialize an empty list to store selected & declined recipes
selected_recipes = []
declined_recipes = []


# function to propose recipes 
def propose_recipe():
    global done # declare var done 
    cursor.execute("SELECT Recipe_Name, Recipe_Ingredients FROM recipes") # select name & ingredients cols from recipe entries 
    rows = cursor.fetchall() # fetch all rows 
    
    while not done: # while done = False: 
        known_recipes = [{'Recipe_Name': row[0], 'Recipe_Ingredients': row[1]} for row in rows] # process all recipe name & ingredients as dict 
        available_recipes = [recipe for recipe in known_recipes if recipe not in selected_recipes and recipe not in declined_recipes] # available recipes = all known recipes not yet selected or declined 
        if not available_recipes: # if no recipes available: 
            print("You've already selected all available recipes.")
            done = True
            break
        
        recipe = random.choice(available_recipes) # randomly select from list of available recipes 
        print(f"Do you want to make {recipe['Recipe_Name']}? (y/n)") # propose recipe to user 
        choice = input().strip().lower() # process input 
        if choice == 'y':
            selected_recipes.append(recipe) # append to selected list 
            print(f"{recipe['Recipe_Name']} added to your list.") 
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
        ingredients = recipe['Recipe_Ingredients'] # access ingredients 
        for ingredient in ingredients.split(","): # split by comma  
            shopping_list.append(ingredient.strip()) # and append to shopping list 
    shopping_list = sorted(list(set(shopping_list))) # remove duplicates and sort the shopping list
    return shopping_list

# main program
print("Welcome to kitchen-pal!")
locate_db()
done = False # declare done as False to trigger loop 
propose_recipe() # invoke propose recipe 
if done: # once done = True: 
    print("Great! You've selected the following recipes:") # review selected recipes 
    for recipe in selected_recipes:
        print(recipe['Recipe_Name'])
    shopping_list = generate_shopping_list() # invoke generate list
    print("\nHere's your shopping list:")
    for item in shopping_list:
        print(item)
else:
    print("You haven't selected any recipes. Have a great day!")

conn.close()

## INSERT INTO recipes (Recipe_Name, Recipe_Ingredients, Recipe_Link) VALUES ("Lemon Garlic Butter Chicken and Brussels Sprouts", "brussels sprouts, olive oil, salt, pepper, paprika, chicken tenderloins, Italian seasoning, red pepper flakes, lemon juice, butter", "https://juliasalbum.com/lemon-garlic-butter-chicken/")y
