from flask import Flask, render_template
app = Flask(__name__)
#SARAHs

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome_student_name(student_name):
    return render_template("welcome.html",student_name=student_name)


@app.route("/roster/<int:grade_view>")
def roster_grade_view(grade_view):
    student1=("Blessy","A-","Senior")
    student2=("Peter","B","Freshman")
    student3=("Zoe","A","Sophmore")
    student4=("Joel","C","Junior")
    student5=("Ashley","B+","Senior")
    student6=("Ashton","F","Junior")
    student7=("Elaine","C+","Sophmore")
    student8=("Samuel","A-","Freshman")
    student9=("Lucas","D","Senior")

    class_roster=[student1,student2,student3,student4,student5,student6,student7, student8, student9]
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == '__main__':
	app.run(debug=True)
