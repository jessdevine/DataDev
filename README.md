# DishLab: 

http://cookbook.jessicadevine.com/

DishLabs soul purpose is to share quick and easy meals, all made with only 5 ingredients. It targerts busy milienals who are too 
occuibed with study, work, socializing and the general chaos of living in the 21st centery to be wasting valuable time in the kitchen. 
All while wanting to maintain a healthy lifestyle with home cooked meals using only the honest active ingredients. 

##

This web application is built with responsive, mobile first design and an edgy aesthetic. Users will be able to view, filter, add, edit, and delete 
recipes. 


#### User Stories 

As a new user I want to be able to:
- Visit a homepage with a site description
- See summaries of recipies
- View all recipies 
- Filter/sort recipes
- Options to search and navigate the site

As a user who wants to add a recipe to the site I want to be able to:
- Add a recipie while navigating through any part of the site
- See a form that allows for input to include all aspects of the recipie
- Have the option to Submit  

As a user who wants to edit or delete an existing recipie I want to be able to:
- Easily find recipies by search or filter 
- See an edit button which brings me to a page with pre populated fields of the selected recipie
- Submit changes or Delete recipie button at the bottom of the form 

A user whos wants to find a recipe for a specfic meal time I want to be able to:
- Select from a meal category on the homepage
- See a selection of only recipie names and cusines
- Drop down arrow on each item to expand on recipe and see all attributes

A user whos wants to filter for a cusine:
- Goes to All Recipes 
- Sees a drop down selection 
- User selects their prefer cusine
- Recipes update based on selected cusine

Wireframes:

http://cookbook.jessicadevine.com/static/images/homepage.png

http://cookbook.jessicadevine.com/static/images/recipes.png

## Features

### Existing Features

- Add a recipie
- Edit existing recipies
- Delete recipes
- Filter/Sort recipes 

### Features Left to Implement
- A user login system
- Searching 

## Technologies Used

[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

[Materialize CSS](https://materializecss.com/)

[JavaScript](https://www.javascript.com/)

[Flask](https://flask.palletsprojects.com/en/1.0.x/)

[Python](https://www.python.org/)

[MongoDB](https://www.mongodb.com/)

[Atlas](https://www.mongodb.com/cloud/atlas)

[Heroku](https://dashboard.heroku.com/)



## Testing
- Tested on all new age desktop and mobile browsers to ensure cross compatibility & functionality.
- Tested to be responsive and to ensure it would be correctly displayed across different mobile screens sizes.
- Each one of the user stories were tested without errors.
- Testing for this project was done manually. The majority of testing covered the different Flask routes. 
- On the homepage if any user selects one of the meals, that being "Breakfast", "Lunch" etc it would route them to a recipies with only recipies under the selected meal.
- On the home page the bottom contains a summaries section in which different cusines were counted from the database
- For text-area and inputs, a max-length was added to restrict input length. 
- For form options like Meal, Cusines and Prep and cook time drop downs were implemented to avoid human error when entering these feilds


## Deployment

### I deployed my site using Heroku

* Create a new app on Heroku 
* If Heroku is not already pre installed in the development environment then run the following CLI command:
```
$ sudo snap install --classic heroku
```
* Login to Heroku Via the command line:
```
$ heroku login 
```

* Create a new Git repository and connect Heroku
```
$ cd my-project/
$ git init
$ heroku git:remote -a datadevelopment
```

Add Requirements.txt
```
$ sudo pip3 freeze —local > requirements.txt
```
Add ProcFile
```
echo web: python app.py > Procfile
```
Deploy Site: 
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
Run Application:
```
$ heroku ps:scale web=1
```
In the Heroku application
Go to Settings > Config Vars
Specify IP & Port:
```
IP    
PORT
MONGODB_URI
```


### Content

- A portion of the content was written by myself and other recipes were obtained from [Pillsbury](https://www.pillsbury.com/recipes/5-ingredient-recipes)

### Media
- The photos used in this site were obtained [Unsplash](https://unsplash.com/)

