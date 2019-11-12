## Imported from Sarah Guthrie's Feature class
from flask import Flask, render_template
from forms import UserSignUpForm, LoginForm, AddCarForm
DEBUG = True
app = Flask(__name__)

#app.config['SECRET_KEY'] = ''

Car =[
{
'user_id': 'Shawn',
'id': '123',
'car_vin':'ABC123',
'model': 'Ford Truck',
'make': '2018',
'color': 'Red',
},
{
'user_id': 'Sarah',
'id': '456',
'car_vin':'TU456',
'model': 'Toyota',
'make': '2016',
'color': 'Black'
}
]
@app.route("/")
def home():
    return render_template('index.html', Car=Car)

@app.route("/Login")
def Login():
    form = LoginForm()
    return render_template('login.html', User=User)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/add-car", methods =['GET','POST'])
def addCar():
    form = AddCarForm()
    return render_template('addCar.html', title='Add A Car', form=form)
