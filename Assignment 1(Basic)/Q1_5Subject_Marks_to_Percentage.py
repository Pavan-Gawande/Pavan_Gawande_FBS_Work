#To find percentage of student based on marks of 5 subject

MaxMarks = int(input("Enter maximum marks : "))

M1 = int(input("Enter the marks of 1st subject : "))
M2 = int(input("Enter the marks of 2nd subject : "))
M3 = int(input("Enter the marks of 3rd subject : "))
M4 = int(input("Enter the marks of 4th subject : "))
M5 = int(input("Enter the marks of 5th subject : "))

Sum = M1 + M2 + M3 + M4 + M5
Percentage = ( Sum / (5*MaxMarks) ) *100

print("Percentage : ", Percentage)