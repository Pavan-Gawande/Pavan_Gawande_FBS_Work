# Python program to find elements in a given set that are not in another set.

def aMinusB(a, b):
    for i in b:
        if(i in a):
            a.remove(i)
    return a

a = set(map(int, input("Enter set a elements : ").split()))
b = set(map(int, input("Enter set b elements : ").split()))

print("Set A : ", a)
print("Set B : ", b)
output = aMinusB(a, b)
print("Output set : ", output)

