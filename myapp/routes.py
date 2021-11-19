from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/loggedin")
@login_required
def log():
    return 'Hi! You are logged in'

@myapp_obj.route("/logout")
def logout():
    logout_user()
    return redirect('/')

@myapp_obj.route("/")
def hello():
    name = 'Travis'
    people = {'Travis' : 25}
    title = 'Studious HomePage'
    return render_template("hello.html", name=name, people=people, title=title)

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login Invalid: Username or Password!')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        flash(f'Login password {form.password.data}')
        return redirect('/')
    return render_template("login.html", form=form)


@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return 'Hi ' + name

@myapp_obj.route("/notes", methods=['GET','POST'])
def flashcard():
    return render_template("notes.html",title='Note Taker')
