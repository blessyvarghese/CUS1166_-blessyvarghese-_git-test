from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route("/Roster/<int:grade_view>")
def roster(grade_view):
    student1=("Peter","A","Sophomore")
    student2= ("Sarah","B","Junior")
    student3= ("Tom", "C", "Senior")
    student4= ("Ashton", "A-", "Freshmen")
    student5= ("Elaine" , "B+", "Junior")
    student6= ("Kevin", "C", "Sophomore")

    Roster= [student1, student2, student3, student4, student5, student6]
    return render_template("roster.html", Roster=Roster, grade_view=grade_view)

if __name__ == '__main__':
	app.run(debug=True)
