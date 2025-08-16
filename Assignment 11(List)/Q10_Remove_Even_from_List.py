# program to print list after removing even numbers.

def evenRem(l1):
    n = len(l1)
    i = 0
    while(n > 0):
        if(l1[i]%2 == 0):
            l1.pop(i)
        else:
            i += 1
        n -= 1
    return l1

l1 = list(map(int, input("Enter the list elements : ").split()))
print("Original Num List : ", l1)
output = evenRem(l1.copy())
print("Original Num List : ", output)