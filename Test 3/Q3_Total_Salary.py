# To find total salary of each employee and combined salary using basic salary 

n = int(input("Enter the no. of employees : "))
salarySum = 0

for i in range(n):
    sal = int(input(f"Enter the salary of employee {i+1} : "))
    if(sal < 20000):
        da = sal*0.1
        ta = sal*0.12
        hra = sal*0.15
        totalSalary = sal + da + ta + hra
    else:
        da = sal*0.15
        ta = sal*0.18
        hra = sal*0.20
        totalSalary = sal + da + ta + hra
    print(f'Total salary of employee {i+1} : {totalSalary}')
    salarySum += totalSalary
print(f'Combined salary of all employees : {salarySum}')