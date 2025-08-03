# program to print list after removing even numbers.

def removeEven(list1):
    n = len(list1)
    i = 0
    while(n > 0):
        if(list1[i]%2 == 0):
            del list1[i]
        else:
            i += 1
        n -= 1
    return list1
    
l = list(map(int, input("Enter list elements separated by spaces : ").split()))
print("Original List : ", l)

print("Final List : ", removeEven(l))