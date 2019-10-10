import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template('index.html',courses=courses)

@app.route("/add_course", methods=["post"])
def add_course():
    id = request.form.get("id")
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    course = Course(id=id,course_number=course_number,course_title=course_title)
    db.session.add(course)
    db.session.commit()
    courses = Course.query.all()
    return render_template('index.html',courses=courses)

@app.route("/register_student/<int:course_id>", methods=['POST','GET'])
def register_student(course_id):
    course = Course.query.get(course_id)
    if request.method == 'GET':
        return render_template('course_details.html',course=course)
    elif request.method == 'POST':
        id = request.form.get("id")
        name = request.form.get('name')
        grade = request.form.get('grade')
        #if id of student already exists, student gets a course added
        if(RegisteredStudent.query.get(id)):
            student = RegisteredStudent.query.get(id)
            course.students.append(student)
        #if id is not of any current student, new student gets created and a course is matched to it
        else:
            student = RegisteredStudent(id=id, name=name, grade=grade)
            course.students.append(student)
            db.session.add(student)
            db.session.commit()
        return render_template('course_details.html', course=course)

if __name__ == '__main__':
	app.run(debug=True)
