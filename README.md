# kitchen-pal
a virtual recipe box

kitchen-pal is a small console program designed for that moment when you sit down to plan your meals and forget every dish you've ever liked. Store your favorite recipes in the SQLite database recipes.db. When you run kitchenPal.py, the program will suggest recipes from the database that you may accept or decline. After you have completed your selections, the program will generate a weekly shopping list. 

## how to use 

### set-up
You will need the following software installed on your machine: 

* [Python](https://www.python.org/downloads/)
* [SQLite](https://www.sqlite.org/download.html) or another database browser
  
Once those items have been installed, clone the kitchen-pal repository to your machine to get cooking. 

### managing your recipe database 

Several recipes have been preloaded for your convenience. To review the existing database: 

1. Navigate to your local repository.
2. Open recipeCodex.db.
3. Use the Browse Data tab to review your recipes.

#### adding new recipes 

1. Insert a new record into the current table using the icons located at the top of the Browse Data Tab.
2. Complete the following fields in the table:
   - **recipe name***
   - **recipe ingredients***
   - **link**  

You may also add new records to your table on the Execute SQL tab by adapting the following SQL command : _INSERT INTO recipes (name, ingredients, link) VALUES ("RECIPE NAME HERE", "INGREDIENT1, INGREDIENT2, INGREDIENT3", "link")_

**Note:** You may choose to omit a recipe link when adding new records to the table. I recommend you include it for your own information. I once made the most wonderful Thai pumpkin soup from an online recipe but lost the link. I consider this to be one of the great tragedies of my life. However, only the **recipe name** and **recipe ingredients** fields are called by the program. 

#### removing recipes 
To discard a recipe, select the row you want to remove then use the icons located at the top of the Browse Data tab to delete. 

You may also discard recipes on the Execute SQL tab by adapting the following SQL command : _INSERT INTO recipes (name, ingredients, link) VALUES ("RECIPE NAME HERE", "INGREDIENT1, INGREDIENT2, INGREDIENT3", "link")_


