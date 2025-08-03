# program to print all numbers which are divisible by m and n in the list.

list1 = list(map(int, input("Enter list elements separated by spaces : ").split()))

m = int(input("Enter the value of m : "))
n = int(input("Enter the value of n : "))

for ele in list1:
    if(ele%m == 0 and ele%n == 0):
        print(ele)
