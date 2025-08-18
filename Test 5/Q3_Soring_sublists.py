def sortSubList(l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if(l[i][2] > l[j][2]):
                l[i], l[j] = l[j], l[i]

l = []
n = int(input("Enter the no. of Elements : "))
for i in range(n):
    temp = list(map(str, input("Enter Employee details : ").split()))
    l.append(temp)
print("Original List : ", l)
sortSubList(l)
print("Sorted List : ", l)