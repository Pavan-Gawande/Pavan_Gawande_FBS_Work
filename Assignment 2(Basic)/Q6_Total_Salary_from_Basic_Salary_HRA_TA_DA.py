# To calculate total salary of an employee from given basic salary.

BasicSalary = float(input("Enter the basic salary of an employee :"))

da = 0.1*BasicSalary
ta = 0.12*BasicSalary
hra = 0.15*BasicSalary

TotalSalary = BasicSalary +  da + ta + hra

print("The total salary of the employee is : ",TotalSalary)