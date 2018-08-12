from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from forms import *
from flask import Flask
from config import Config
from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Models.models import User

app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))

# Log-in for users and admin
@app.route('/users/login', methods=['GET', 'POST'])
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
@login_required
def index():
    return render_template('index.html', title='Dashboard')


@app.route('/users/register')
def register():
    form = RegisterForm()
    return render_template('registration.html', title='Register', form=form)
# ADMIN

# Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html', title='Sign In')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)


