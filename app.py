from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required
from Controllers.Admin_Controller import admin_post
from forms import LoginForm, RegisterForm
from flask import Flask
from config import Config
from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import Models.models
from Models.models import User

app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))

@app.route('/users/login', methods=['GET', 'POST'])
@app.route('/admin', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('dashboard.html', title='Sign In')


#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()


