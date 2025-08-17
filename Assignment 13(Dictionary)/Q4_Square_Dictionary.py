# Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

dict1 = dict()
n = int(input("Enter the value of N : "))
for i in range(1, n+1):
    dict1[i] = i*i
print("Square dictionary : ",dict1)