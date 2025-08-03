# program to remove all occurrences of a given element in the list.

def remOccurrences(list1, ele):
    n = len(list1)
    i = 0
    while(n > 0):
        if(list1[i] == ele):
            list1.pop(i)
        else:
            i += 1
        n -= 1
    return list1

list1 = list(map(int, input("Enter list elements separated by spaces : ").split()))
ele = int(input("Enter the elemnt to remove : "))

print("Final List : ", remOccurrences(list1, ele))