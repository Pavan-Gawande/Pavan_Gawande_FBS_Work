# program to find sum of all elements of list

n = int(input("Enter the no. of element : "))
l = []
for i in range(n):
    l.append(int(input()))

sum = 0
for ele in l:
    sum += ele

print("Sum of elements : ", sum)