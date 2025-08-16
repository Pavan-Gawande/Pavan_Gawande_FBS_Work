# Program to Sort the List According to the Second Element in Sublist

def sortBy2(l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if(l[i][1] > l[j][1]):
                l[i], l[j] = l[j], l[i]
    return l

n = int(input("Enter the no of Elements : "))
main = []
for i in range(n):
    t = list(map(int, input(f"Enter element {i+1} (a b) : ").split()))
    main.append(t)
output = sortBy2(main.copy())
print("Original List : ", main)
print("Sorted List : ", output)