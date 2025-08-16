# program to create three lists of numbers, their squares and cubes

def powList(l, pow):
    output = []
    for i in l:
        output.append(i**pow)
    return output

l1 = list(map(int, input("Enter the list elements : ").split()))
print("Original Num List : ", l1)
squareList = powList(l1, 2)
print("Square List : ", squareList)
cubeList = powList(l1, 3)
print("Cube List : ", cubeList)

