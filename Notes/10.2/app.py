#USING FLASK
import os
from flask import Flask, render_template, request, redirect

# provides access to the create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#intialize the database connection



app = Flask(__name__)

@app.route("/")
def index():
    flights= db.execute("SELECT * from flights")
    return render_template('index.html', flights= flights)

@app.route("/add_flight", methods=["post"])
def add_flight():
    #get info from the form
    origin= request.form.get("origin")
    destination= request.form.get("destination")
    duration= request.form.get("duration")

    #update the database
    flights = db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)")

def main():
    if(len(sys,argv)==2):
        print(sys,argv)
