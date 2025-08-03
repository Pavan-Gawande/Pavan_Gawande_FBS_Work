# program to find maximum and minimum element in a list.

n = int(input("Enter the no. of element : "))
l = []
for i in range(n):
    l.append(int(input()))

min = l[0]
max = l[0]
for i in range(1, n):
    if(max < l[i]):
        max = l[i]
    elif(min > l[i]):
        min = l[i]

print("Minimum : ", min)
print("Maximum : ", max)