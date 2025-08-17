# Python program to remove the intersection of a second set with a first set.

def intersection(a, b):
    c = set()
    for i in b:
        if(i in a):
            c.add(i)
    return c

a = set(map(int, input("Enter set a elements : ").split()))
b = set(map(int, input("Enter set b elements : ").split()))

print("Set A : ", a)
print("Set B : ", b)
output = intersection(a, b)
print("Output set(Intersection) : ", output)