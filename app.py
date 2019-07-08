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
  
  
  
  

  

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)