# Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

def missingNums(s1, s2):
    comm = set()
    for i in s1:
        if(i in s2):
            comm.add(i)
    for i in comm:
        s1.remove(i)
        s2.remove(i)
    return s1, s2

s1 = set(map(int, input("Enter elements of set1 : ").split()))
s2 = set(map(int, input("Enter elements of set2 : ").split()))

missS2, missS1 = missingNums(s1, s2)
print("Missing elements in set1 are : ", missS1)
print("Missing elements in set2 are : ", missS2)
