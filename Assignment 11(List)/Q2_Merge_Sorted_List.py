# Program to Merge Two Lists and Sort it

def mergeLists(l1, l2):
    output = []
    if(len(l2) < len(l1)):
        l2, l1 = l1, l2
    i, j = 0, 0
    n = len(l1)
    while(i<n):
        if(l1[i] < l2[j]):
            output.append(l1[i])
            i += 1
        else:
            output.append(l2[j])
            j += 1
    output.extend(l2[j:])
    return output

list1 = list(map(int, input("Enter the list1 elements: ").split()))
list2 = list(map(int, input("Enter the list2 elements: ").split()))

outputList = mergeLists(list1, list2)

print("Original List1 : ", list1)
print("Original List2 : ", list2)
print("Final Merged and Sorted List: ", outputList)