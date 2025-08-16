# Program to Find the Intersection of Two Lists

def intersection(l1, l2):
    output = []
    for i in l1:
        if(i in l2):
            output.append(i)
            l2.remove(i)
    return output

l1 = list(map(int, input("Enter the list1 elements: ").split()))
l2 = list(map(int, input("Enter the list2 elements: ").split()))
print("Original list1 : ", l1)
print("Original list2 : ", l2)
output = intersection(l1, l2.copy())
print("Intersection list : ", output)