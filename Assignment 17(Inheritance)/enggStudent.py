from student import Student

class EnggStudent(Student):
    def __init__(self, id=0, name="", age=0, percentage=0, branch="", InternalMarks=0):
        super().__init__(id, name, age, percentage)
        self.branch = branch
        self.InternalMarks = InternalMarks
        self.percentage = 0.8*self.percentage + self.InternalMarks
    
    def accept(self):
        super().accept()
        self.branch = input("Enter the branch : ")
        self.InternalMarks = int(input("Enter the internal marks : "))
        self.percentage = 0.8*self.percentage + self.InternalMarks
        
    def calculateRank(self):
        return super().calculateRank()
    
    def display(self):
        print(f'{self.id}:{self.name} from {self.branch} branch has {self.InternalMarks} internal marks and scored {self.percentage}%')
    
    def __str__(self):
        print(f'{self.id}:{self.name} is from {self.branch} branch')

if(__name__ == "__main__"):
    stud1 = EnggStudent(101, "pavan", 21, 80, "Comp",18)
    stud1.display()
    rank = stud1.calculateRank()
    print(rank)
    