# program to find the second largest element in the list.

n = int(input("Enter the no. of element : "))
l = []
for i in range(n):
    l.append(int(input()))

max = l[0]
for i in range(1, n):
    if(max < l[i]):
        sec_max = max
        max = l[i]
    elif(sec_max < l[i]):
        sec_max = l[i]
print("Maximum : ", max)
print("Second Maximum : ", sec_max)