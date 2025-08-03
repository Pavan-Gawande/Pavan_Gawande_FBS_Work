# program to create three lists of numbers, their squares and cubes

def powList(list1, power):
    l = []
    for i in list1:
        l.append(i**power)
    return l

l1 = list(map(int, input("Enter list elements separated by spaces : ").split()))
print("Original List : ", l1)

l2 = powList(l1, 2)
print("Square List : ", l2)

l3 = powList(l1, 3)
print("Cube List : ", l3)
