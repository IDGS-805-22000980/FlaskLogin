from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms import EmailField
from wtforms import validators

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[validators.DataRequired()])
    password = StringField('Password', validators=[validators.DataRequired()])

