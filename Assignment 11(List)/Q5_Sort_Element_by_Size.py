# Program to Sort a List According to the Length of the Elements within the list.
def sortByLength(l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if(len(l[i]) > len(l[j])):
                l[j], l[i] = l[i], l[j]

l = list(map(str, input("Enter the list elements: ").split()))
print("Original list : ", l)
sortByLength(l)
print("Sorted List : ", l)