import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

#Connecting to MongoDB "Online Cookbook"

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root:537743root@jesscluster-o9ja6.mongodb.net/cookbook?retryWrites=true'

mongo = PyMongo(app)

# Get Recipies 

@app.route('/')
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

  

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)