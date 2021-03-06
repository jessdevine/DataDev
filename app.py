import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

#Connecting to MongoDB "Online Cookbook"


app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


mongo = PyMongo(app)

# Home Page

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("home.html",
    count_recipies=mongo.db.recipes.count(),
    count_breakfasts=mongo.db.recipes.count({"meal": "Breakfast"}),
    count_lunches=mongo.db.recipes.count({"meal": "Lunch"}),
    count_dinners=mongo.db.recipes.count({"meal": "Dinner"}),
    count_american=mongo.db.recipes.count({"cuisine":"American"}),
    count_deserts=mongo.db.recipes.count({"meal":"Dessert"}),
    count_vegan=mongo.db.recipes.count({"cuisine": "Vegan"}),
    count_asian=mongo.db.recipes.count({"cuisine": "Asian"}),
    count_mediterranean=mongo.db.recipes.count({"cuisine": "Mediterranean"}),
    count_keto=mongo.db.recipes.count({"cuisine": "Keto"}),
    count_italian=mongo.db.recipes.count({"meal": "Italian"}))




# All Recipes 

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
                           recipes=mongo.db.recipes.find())
                           
                           
# Add Recipe 

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           recipes=mongo.db.recipes.find())
                           

# Insert Recipe and redirect

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
  
  
  
#  Edit Recipe route 
  
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines =  mongo.db.cuisines.find()
    return render_template('editrecipe.html', recipe=the_recipe, cuisine=all_cuisines)
 

# Update Recipe with pre populated fields
 
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'name':request.form.get('name'),
        'description':request.form.get('description'),
        'serves':request.form.get('serves'),
        'preptime':request.form.get('preptime'),
        'cooktime':request.form.get('cooktime'),
        'meal':request.form.get('meal'),
        'ingredient_1':request.form.get('ingredient_1'),
        'ingredient_2':request.form.get('ingredient_2'),
        'ingredient_3':request.form.get('ingredient_3'),
        'ingredient_4':request.form.get('ingredient_4'),
        'ingredient_5':request.form.get('ingredient_5'),
        'method_1':request.form.get('method_1'),
        'method_2':request.form.get('method_2'),
        'method_3':request.form.get('method_3'),
        'cuisine':request.form.get('cuisine'),
        'author':request.form.get('author')

    })
    return redirect(url_for('get_recipes'))  

 
# Delete via recipie ID  
 
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
    


# MEALS

# Breakfast
@app.route('/breakfast_meals')
def breakfast_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "Breakfast"}))

# Lunch
@app.route('/lunch_meals')
def lunch_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "Lunch"}))
                           

# Dinner
@app.route('/dinner_meals')
def dinner_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "Dinner"}))
                           
# Deserts
@app.route('/dessert_meals')
def dessert_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "Dessert"}))
        
        
# MEALS
                   
# American
@app.route('/american_meals')
def american_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"cuisine": "American"}))

# Asian Street Food
@app.route('/asian_meals')
def asian_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"cuisine": "Asian"}))
                           
# Italian
@app.route('/italian_meals')
def italian_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"cuisine": "Italian"}))
                           
                           
# Vegan
@app.route('/vegan_meals')
def vegan_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"cuisine": "Vegan"}))
                           
# Keto
@app.route('/keto_meals')
def keto_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"cuisine": "Keto"}))
                          
                           
# Indian
@app.route('/indian_meals')
def indian_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"cuisine": "Indian"}))

                           
                           
# Mediterranean
@app.route('/mediterranean_meals')
def mediterranean_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"cuisine": "Mediterranean"}))

    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)