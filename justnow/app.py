""" This module contains all the view functions for the Yummy recipe app"""
from functools import wraps
from flask import Flask
from flask import render_template, session, flash, redirect, url_for, request
from models import User

app = Flask(__name__)
app.secret_key = 'thisismysecretdonteventhinkaboutit'
USERS = {}


def register(name, username, password, rpt_password):
    """ This function handles user registration"""
    if name and username and password and rpt_password:
        if len(username) > 3 and len(username) < 11:
            if len(password) > 2 and len(password) < 11:
                if password == rpt_password:
                    USERS[username] = User(name, username, password)
                    return "Registration successful"
                return "Passwords don't match"
            return "Password should be 2 to 10 characters"
        return "Username should be 4 to 10 characters"
    return "None input"


def login(username, password):
    """ Handles user login """
    if username and password:
        if USERS.get(username):
            if USERS[username].password == password:
                return "Login successful"
            return "Wrong password"
        return "User not found"
    return "None input"


@app.route('/')
def home():
    """ Handles the home route """
        # if session.get('username'):
        #     return redirect(url_for('categories'))
        # else:
    return render_template('home.html')


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    """ Handles the sign_in route """
    if request.method == 'POST':
        result = login(request.form['username'], request.form['password'])
        if result == "Login successful":
            session['username'] = request.form['username']
            return redirect(url_for('categories'))
        flash(result, 'warning')
    return render_template('login.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """ Handles the sign_up route """
    if request.method == 'POST':
        result = register(request.form['name'], request.form['username'],
                          request.form['password'], request.form['rpt_password'])
        if result == "Registration successful":
            flash(result, 'info')
            return redirect(url_for('sign_in'))
        flash(result, 'warning')
    return render_template('register.html')


def login_required(func):
    """ Decorator function to ensure some routes are only accessed by logged in users """
    @wraps(func)
    def decorated_function(*args, **kwargs):
        """ Modified descriprition of the decorated function """
        if not session.get('username'):
            flash('Login to continue', 'warning')
            return redirect(url_for('sign_in', next=request.url))
        return func(*args, **kwargs)
    return decorated_function


@app.route('/categories', methods=['GET', 'POST'])
@login_required
def categories():
    """ Handles displaying recipe categories """
    return render_template('categories.html', recipe_categories=USERS[session['username']].recipe_categories)


@app.route('/add_category', methods=['GET', 'POST'])
@login_required
def add_category():
    """ Handles new  recipe_category creation requests """
    if request.method == 'POST':
        result = USERS[session['username']].add_recipe_category(
            request.form['title'])
        if result == 'recipe_category added':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('categories'))
    return render_template('add_category.html')


@app.route('/edit_category/<title>', methods=['GET', 'POST'])
@login_required
def edit_recipe_category(title):
    """ Handles request to edit recipe categories """
    session['recipe_category_title'] = title
    if request.method == 'POST':
        result = USERS[session['username']].edit_recipe_category(session['recipe_category_title'],
                                                                 request.form['title'])
        if result == 'recipe_category edited':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('dashboard'))
    return render_template('edit_recipe_category.html')


@app.route('/delete_recipe_category/<title>', methods=['GET', 'POST'])
@login_required
def delete_recipe_category(title):
    """ Handles request to delete a category_recipe"""
    result = USERS[session['username']].delete_recipe_category(title)
    if result == "recipe category deleted":
        flash(result, 'info')
    else:
        flash(result, 'warning')
    return redirect(url_for('categories'))


@app.route('/recipes/<recipe_category_title>', methods=['GET', 'POST'])
@login_required
def recipes(recipe_category_title):
    """ Handles displaying recipes """
    session['current_recipe_category_title'] = recipe_category_title
    return render_template('recipes.html', recipes=USERS[session['username']]
                           .recipe_categories[recipe_category_title].recipes)


@app.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    """ Handles new recipe creation requests """
    if request.method == 'POST':
        result = USERS[session['username']].recipe_category[session['current_recipe_category_title']].add_recipe(
            request.form['description'])
        if result == 'recipe added':
            flash(result, 'info')
        else:
            flash(result, 'warning')
        return redirect(url_for('view_recipes', recipe_category_title=session['current_recipe_category_title']))
    return render_template('add_recipe.html', recipes=USERS[session['username']].recipe_category[session['current_recipe_catrgory_title']].recipes)

@app.route('/edit_recipe/<description>', methods=['GET', 'POST'])
@login_required
def edit_recipe(description):
    """ Handles request to edit a recipe """
    session['description']=description
    if request.method == 'POST':
        des_result=(USERS[session['username']].recipe_category[session['current_recipe_category_title']].
                      update_description(session['description'], request.form['description']))
        status_result=(USERS[session['username']].recipe_category[session['current_recipe_category_title']].
                         update_status(session['description'], request.form['status']))
        if des_result == 'recipe updated' or status_result == 'recipe updated':
            flash('recipe updated', 'info')
        else:
            flash(des_result, 'warning')
        return redirect(url_for('edit_recipe', recipe_category_title=session['current_recipe_category_title']))
    return render_template('edit_recipe.html', item=USERS[session['username']]
                           .recipe_category[session['current_recipe_category_title']].recipes[description],
                           recipes=USERS[session['username']].
                           recipe_category[session['current_recipe_category_title']].recipes)



@app.route('/recipe/<description>', methods=['GET', 'POST'])
@login_required
def recipe_details():
    return render_template("details.html", details=details)
                               

# @app.route('/recipe/<description>', methods=['GET', 'POST'])
# @login_required
# def delete_recipe(description):
#     """ Handles request to delete a recipe """
#     result = USERS[session['username']].recipe_category[session['current_recipe_category_title']].delete_item(
#         description)
#     if result == 'Item deleted':
#         flash(result, 'info')
#     else:
#         flash(result, 'warning')
#     return redirect(url_for('view_recipe', recipe_category_title=session['current_recipe_category_title']))


# @app.route('/logout')
# @login_required
# def logout():
#     """ logs out a user """
#     session.pop('username')
#     flash('You have logged out', 'warning')
#     return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)
