# program to remove duplicates from the list.

l = list(map(int, input("Enter list elements separated by spaces : ").split()))

ul = []

for i in l:
    if(i not in ul):
        ul.append(i)
    
print("Original list : ",l)
print("Unique list : ", ul)