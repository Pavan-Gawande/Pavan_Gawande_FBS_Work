from student import Student

class MedStudent(Student):
    def __init__(self, id=0, name="", age=0, percentage=0, specialization="", marksOfInternship=0):
        super().__init__(id, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship
        self.percentage = (self.percentage*5 + self.marksOfInternship) // 6
    
    def display(self):
        print(f'{self.id}:{self.name} from {self.specialization} specialization has {self.marksOfInternship} internship marks and scored {self.percentage}%')
        
    def calculateRank(self):
        return super().calculateRank()
    
    def accept(self):
        super().accept()
        self.specialization = input("Enter the specialization : ")
        self.marksOfInternship = int(input("Enter the internship marks : "))
        self.percentage = (self.percentage*5 + self.marksOfInternship) // 6
    
    def __str__(self):
        print(f'{self.id}:{self.name} is from {self.specialization} specialization')

if(__name__ == "__main__"):
    m1 = MedStudent(1, "pg", 21, 80, "cardialogy", 60)
    m1.display()
    r = m1.calculateRank()
    print(r)
    