from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign in")

class RegisterForm(FlaskForm):
    username = StringField("Username",validators = [DataRequired()])
    password = PasswordField("Password",validators =[DataRequired()])
    submit = SubmitField("Register")

class FileForm(FlaskForm):
    file = FileField('File', validators=[
        FileRequired(),
        FileAllowed(['md'], '.md only!')
    ])
    submit = SubmitField('Upload')

class SearchForm(FlaskForm):
    text = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Search')

class PasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Change")