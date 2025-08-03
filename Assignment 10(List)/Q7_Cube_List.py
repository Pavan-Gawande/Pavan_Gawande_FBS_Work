# program to create a new list from existing list which contains cube of
# each number of list.

l = list(map(int, input("Enter list elements separated by spaces : ").split()))


cl = []

for i in l :
    cl.append(i**3)

print("Original list : ", l)
print("Cube list : ", cl)