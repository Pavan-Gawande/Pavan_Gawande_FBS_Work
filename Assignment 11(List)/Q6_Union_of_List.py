# Program to Find the Union of two Lists
def unionList(l1, l2):
    if(len(l2) > len(l1)):
        l1, l2 = l2, l1
    for i in l1:
        if(i in l2):
            l2.remove(i)
    l1.extend(l2)
    return l1

l1 = list(map(int, input("Enter the list1 elements: ").split()))
l2 = list(map(int, input("Enter the list2 elements: ").split()))
output = unionList(l1.copy(), l2.copy())
print("Original list1 : ", l1)
print("Original list2 : ", l2)
print("Union list : ", output)