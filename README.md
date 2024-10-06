# kitchen-pal
a virtual recipe box

kitchen-pal is a small console program designed for that moment when you sit down to plan your meals and forget every dish you've ever liked. Store your favorite recipes in the SQLite database recipes.db. When you run kitchenPal.py, the program will suggest recipes from the database that you may accept or decline. After you have completed your selections, the program will generate a weekly shopping list. 

## how to use 

### set-up
You will need the following software installed on your machine: 

* Python [https://www.python.org/downloads/]
* SQLite [https://www.sqlite.org/download.html]****

Once those items have been installed, clone the kitchen-pal repository to your machine to get cooking. 

### managing your recipe database 

Several recipes have been preloaded for your convenience. To review the existing database: 

1. Navigate to your local repository.
2. Open recipes.db.
3. Use the Browse Data tab to review your recipes.

#### adding new recipes 

4. Insert a new record into the current table using the icons located at the top of the Browse Data Tab.
5. Complete the name, ingredients, and link fields.

**Note:** You may also add new records to your table on the Execute SQL tab by adapting the following SQL command : _INSERT INTO recipes (name, ingredients, link) VALUES ("RECIPE NAME HERE", "INGREDIENT1, INGREDIENT2, INGREDIENT3", "link")_
