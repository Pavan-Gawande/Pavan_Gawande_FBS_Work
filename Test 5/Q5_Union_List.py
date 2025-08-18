def union(l1, l2):
    u = []
    if(len(l1) > len(l2)):
        l1, l2 = l2, l1
    for i in l1:
        if(i in l2):
            l2.remove(i)
        u.append(i)
    u.extend(l2)
    return u

l1 = list(map(int, input("Enter list 1 elements : ").split()))
l2 = list(map(int, input("Enter list 2 elements : ").split()))
print("List 1 : ", l1)
print("List 2 : ", l2)
unionList = union(l1.copy(), l2.copy())
print("Union List : ", unionList)