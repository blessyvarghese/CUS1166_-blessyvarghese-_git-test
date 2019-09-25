class Student:
    def __init__ (self, StudentName, StudentGrade):
        self.StudentName = StudentName
        self.StudentGrade = StudentGrade
    def SetGrade (self, grade):
        self.StudentGrade = grade
    def GetGrade (self):
        return (self.StudentGrade)
    def PrintStudentInfo(self):
        return (self.StudentName , self.StudentGrade)
