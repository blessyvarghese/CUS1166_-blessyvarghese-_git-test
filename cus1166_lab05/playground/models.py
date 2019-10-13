from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String)
    course_title = db.Column(db.String)

    #relationship
    students = db.relationship('RegisteredStudent', secondary='link')

class RegisteredStudent(db.Model):
    __tablename__ = 'registeredstudent'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grade = db.Column(db.Integer)

    #relationship
    courses = db.relationship('Course', secondary='link')

class Enrollment(db.Model):
   __tablename__ = 'link'
   course_id = db.Column, db.Integer, db.ForeignKey('course.id'), primary_key=True)

   #reltioanship
   registeredstudent_id = db.Column(db.Integer, db.ForeignKey('registeredstudent.id'), primary_key=True)
