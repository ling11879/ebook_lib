from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template, flash, redirect
from Controllers.Admin_Controller import admin_post
from forms import LoginForm, RegisterForm
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import Models.models

# Admin
@app.route('/admin')
def admin():
    return admin_post()

@app.route('/admin', methods=['GET', 'POST'])
@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/dashboard')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/dashboard')
def index():
    return render_template('dashboard.html', title='Dashboard')

# User
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('registration.html', title='Register', form=form)



# Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run()