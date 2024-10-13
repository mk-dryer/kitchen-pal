# kitchen-pal
a virtual recipe box

kitchen-pal is a small console program designed for that moment when you sit down to plan your meals and forget every dish you've ever liked. Store your favorite recipes in the recipes.db database. When you run kitchenPal.py, the program will suggest recipes from the database that you may accept or decline. After you have completed your selections, the program will generate a weekly shopping list. 

## How to Use kitchen-pal 

### Setup
You will need the following software installed on your machine: 

* [Python](https://www.python.org/downloads/)
* [SQLite](https://www.sqlite.org/download.html) or your preferred database browser
  
Once those items have been installed, clone the kitchen-pal repository to your machine to get cooking. 

### Managing Your Recipe Table 
**Note:** This section presumes you are working in a SQLite browser.

#### Reviewing Existing Recipes

Several recipes have been preloaded for your convenience. To review the existing database: 

1. Navigate to your local kitchen-pal repository.
2. Open recipeCodex.db.
3. Use the Browse Data tab to review your recipes.

#### Adding New Recipes 

1. Insert a new record into the current table using the icons located at the top of the Browse Data tab.
2. Complete the following fields in the table:
   - **Recipe_Name**
   - **Recipe_Ingredients**
   - **Recipe_Link** (optional)  

You may also add new records to your table on the Execute SQL tab by adapting the following SQL command: _INSERT INTO recipes (Recipe_Name, Recipe_Ingredients, Recipe_Link) VALUES ("RECIPE NAME HERE", "INGREDIENT1, INGREDIENT2, INGREDIENT3", "link")_

**Note:** You may omit a recipe link when adding new records to the table because only the **Recipe_Name** and **Recipe_Ingredients** fields are utilized by the program. However, I recommend you include a link for your own information. I once made the most wonderful Thai pumpkin soup from an online recipe but lost the link. I consider this to be one of the great tragedies of my life.

#### Removing Recipes 
To discard a recipe, select the row you want to remove then use the icons located at the top of the Browse Data tab to delete. 

You may also discard recipes on the Execute SQL tab by adapting the following SQL command : _INSERT INTO recipes (Recipe_Name, Recipe_Ingredients, Recipe_Link) VALUES ("RECIPE NAME HERE", "INGREDIENT1, INGREDIENT2, INGREDIENT3", "link")_

### Launching kitchenPal.py

Once you are satisifed with the contents of your database (or just hangry), you are ready to execute the main program. 

1. Navigate to your local kitchen-pal repository.
2. Select all of the text in the File Explorer browser bar field and type "cmd".
3. Hit enter to open a command line interface. 
4. Type the command "py kitchenPal.py" to launch the program.

kitchen-pal will now suggest recipes from your database of known recipes. You will respond with a simple yes (Y) or no (N) selection. You may kill the program at any point by using "Ctrl+C" on your keyboard. 

### Troubleshooting 

- Be mindful of where you store your local copies of kitchenPal.py and recipesCodex.db. The program cannot connect to the database unless both files are located in the same directory.
