from enggStudent import EnggStudent
from medStudent import MedStudent

class College:
    students = []
    
    def __init__(self, ccode, cname):
        self.ccode = ccode
        self.cname = cname
    
    def addStudent(self):
        ch = input("Enter the field of student Medical or Engineering (e/m) : ")
        sid = int(input("Enter the student id : "))
        sname = input("Enter the student name : ")
        age = int(input("Enter the age of student : "))
        percentage = float(input("Enter the percentage of student : "))
        if(ch == 'e'):
            branch = input("Enter the branch of student : ")
            intMarks = int(input("Enter the internal marks : "))
            s1 = EnggStudent(sid, sname, age, percentage, branch, intMarks)
        else:
            specialization = input("Enter the specialization of the student : ")
            intsMarks = int(input("Enter the marks of internship : "))
            s1 = MedStudent(sid, sname, age, percentage, specialization, intsMarks)
        College.students.append(s1)
        print("Student added successfully . . \n")
    
    def getStudent(self):
        id = int(input("Enter the student id : "))
        for stud in College.students:
            if(stud.id == id):
                print(stud)
                break
        else:
            print("Student not found . .!!")
    
    def removeStudent(self):
        id = int(input("Enter the student id : "))
        i = 0
        for stud in College.students:
            if(stud.id == id):
                del College.students[i]
                print("student removed successfully . .")
                break
            i += 1
        else:
            print("Student not found . .!!")
    
    def __str__(self):
        return f'{self.ccode}:{self.cname} has {len(College.students)} students . .'
    

if(__name__ == "__main__"):
    c1 = College(403, 'SAE')
    c1.addStudent()
    c1.addStudent()
    c1.removeStudent()
    c1.removeStudent()
    print(c1)