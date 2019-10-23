from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Form for User Sign Up
class UserSignUpForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    name= StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Create Account')

# Form for Log In Form
class LoginForm(FlaskForm):
    ## username= StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# Form for adding Car
class AddCarForm(FlaskForm):
    ## username= StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    user_Name = StringField('Name', validators= [DataRequired()])
    make = StringField('Make', validators= [DataRequired()])
    model = StringField('Model', validators= [DataRequired()])
    color = StringField('Color', validators= [DataRequired()])
    car_vin = StringField('Car VIN', validators= [DataRequired()])
    submit = SubmitField('Add Car')
