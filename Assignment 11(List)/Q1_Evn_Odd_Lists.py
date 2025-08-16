# Program to Put Even and Odd elements of a List into two Different Lists

def separate(list1):
    el = []
    ol = []
    for i in list1:
        if(i%2 == 0):
            el.append(i)
        else:
            ol.append(i)
    return el,ol

l = list(map(int, input('Enter list Elements : ').split()))
evenList, oddList = separate(l)

print("Original List : ", l)
print("Even Element List : ", evenList)
print("Odd Element List : ", oddList)