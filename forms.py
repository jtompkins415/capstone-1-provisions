from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length, Email

class UserForm(FlaskForm):
    '''Form for user creation and submition'''

    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[Length(min=1)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    user_city = StringField('City')
    user_state = StringField ('State')

class BeerForm(FlaskForm):
    '''Form for beer creation and submition'''

    beer_name = StringField('Name of Beer')
    brewery = StringField('Brewery')
    style = StringField('Style')
    abv = FloatField('ABV')
    price = FloatField('Price(USD)')
    description = TextAreaField('Description')


class LoginForm(FlaskForm):
    '''Form for user login'''

    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(),Length(min=1)])

class UserEditForm(FlaskForm):
    '''Form for editing user information'''

    username = StringField('New Username')
    email = StringField('New Email', validators=[Email()])
    first_name = StringField('New First Name')
    last_name = StringField('New Last Name')
    user_city = StringField('New City')
    user_state = StringField('New State')

    



