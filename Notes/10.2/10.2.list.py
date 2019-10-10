import os
import sys
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
#DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')




#use scoped_session to mange multiple connection in the DATABASE_U




def create_database():
    db.execute("CREATE TABLE flights (origin VARCHAR(30), destination VARCHAR(30), duration INT(6))")


def populate():
    f = open("flights.csv")
    reader - csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("insert into flights (origin, destination, durations) VALUES(:origin, :destination, :duration)"),
        {"origin" : origin, "destination" : destination, "duration" : int(duration)})
    db.commit()


def list():
    flights = db.execute("Select * from flights")
    print("\nCurrent flights in the database\n")
    for flightin flights:
        print(f"Flight From: {flight.origin} to )
