# User Authentication APIs
from flask import jsonify, redirect, render_template, url_for
from flask_login import LoginManager, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_bcrypt import Bcrypt
from models import User, users

login_manager = LoginManager()
bcrypt = Bcrypt()

# callback to reload user's data
@login_manager.user_loader
def load_user(user_id):
    # return User.get(user_id)
    if user_id not in users:
        return

    user = User()
    user.id = user_id
    # print(jsonify(user))
    return user


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        print('username = ', username)
        print('password = ', users[username]['password'])
        if username in users and form.password.data == users[username]['password']:
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('admin'))
        # user = User.query.filter_by(username=form.username.data).first()
    #     if user:
    #         if bcrypt.check_password_hash(user.password, form.password.data):
    #             login_user(user)
    #             return redirect(url_for('admin'))
    print("wrong credentials")
    return render_template('login.html', form=form)


def logout():
    logout_user()
    return redirect(url_for('upload_file'))