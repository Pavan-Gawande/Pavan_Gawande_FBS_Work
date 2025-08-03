# program to create a duplicate of an existing list. It should not point to same list.

list1 = list(map(int, input("Enter list elements separated by spaces : ").split()))
list2 = list1.copy()

print("Original List : ", list1)
print("Copy List     : ", list2)

print("Memory address of list1 : ", id(list1))
print("Memory address of list2 : ", id(list2))