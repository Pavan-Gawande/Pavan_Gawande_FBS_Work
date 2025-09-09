class Student:
    def __init__(self, id=0, name="", age=0, percentage=0):
        self.id = id
        self.name =name
        self.age = age
        self.percentage = percentage
    
    def display(self):
        print(f'{self.id}:{self.name} of age {self.age} scored {self.percentage}')
    
    def accept(self):
        self.id = int(input("Enter the student id : "))
        self.name = input("Enter the student name : ")
        self.age = int(input("Enter the age of student : "))
        self.percentage = float(input("Enter the percentage of student : "))
    
    def calculateRank(self):
        if(self.percentage>=85 and self.percentage<=100):
            return "First Class with Distinction"
        elif(self.percentage>=70 and self.percentage<85):
            return "First Class"
        elif(self.percentage>=55 and self.percentage<70):
            return "Higher Second Class"
        elif(self.percentage>=40 and self.percentage<55):
            return "Second Class"
        else:
            return "Fail"
        
    def __str__(self):
        print(f'{self.id}:{self.name} of age {self.age} score {self.percentage}')
    

if(__name__ == "__main__"):
    s1 = Student(1,"pg",21,85)
    s1.display()
    rank = s1.calculateRank()
    print(rank)
    
    s2 = Student()
    s2.display()
    s2.accept()
    s2.display()