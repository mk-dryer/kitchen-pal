# KitchenPal
A virtual recipe box.

KitchenPal is a small console program designed to assist you with weekly meal planning. Store your favorite recipes in the Recipe Codex. KitchenPal will suggest recipes from the database for you to review. When you're ready, KitchenPal will generate a weekly shopping list. 

**Note: This guide is written for users on a Windows operating system.**

## How to Use

### Getting Set Up

You will need the following software installed on your machine: 

* [Python](https://www.python.org/downloads/)
* [SQLite Browser](https://sqlitebrowser.org/) or your preferred database browser
  
Once those items have been installed, clone the kitchen-pal repository to your machine to get cooking. 

### Managing your Recipe Table 
**Note:** This section presumes you are working in a SQLite browser.

Several recipes have been preloaded for your convenience. To review the existing database: 

1. Navigate to your local kitchen-pal repository.
2. Open recipeCodex.db.
3. Use the Browse Data tab to review your recipes.

#### Adding New Recipes 

Use the following steps to add new recipes to your personal database: 

1. Insert a new record into the current table using the icons located at the top of the Browse Data tab.
2. Complete the following fields in the table:
   - **RecipeName**
   - **RecipeIngredients**
   - **RecipeLink** (optional)  

You may also add new records to your table on the Execute SQL tab with the following SQL command: _INSERT INTO recipes (RecipeName, RecipeIngredients, RecipeLink) VALUES ("RECIPE NAME HERE", "INGREDIENT1, INGREDIENT2, INGREDIENT3", "link")_

**Note:** As of version 2.0.0, only the **RecipeName** and **RecipeIngredients** fields are required. However, I highly recommend you include a link for your own information. I once made the most wonderful Thai pumpkin soup from an online recipe but lost the link. I consider this to be one of the great tragedies of my life.

#### Removing Recipes 
Use the following steps to discard a recipe: 

1. Select the row you want to remove.
2. Use the icons located at the top of the Browse Data tab to delete. 

You may also discard recipes on the Execute SQL tab by adapting the following SQL command : _DELETE FROM recipes WHERE RecipeName = "RECIPE NAME HERE";_

### Launching kitchenPal.py

Once you are satisifed with the contents of your database (or just hangry), you are ready to execute the main program. 

1. Navigate to your local kitchen-pal repository.
2. Select all of the text in the File Explorer path bar field and type "cmd".
3. Hit enter to open a command line interface. 
4. Type the command "py kitchenPal.py" to launch the program.

### Troubleshooting 

- Be mindful of where you store your local copies of kitchenPal.py and recipesCodex.db. The program cannot connect to the database unless both files are located in the same directory.
