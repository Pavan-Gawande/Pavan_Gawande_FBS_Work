# Program to Find the Second Largest Number in a List Using Bubble Sort

def secLargest(l):
    n = len(l)
    for i in range(1,min(n, 3)):
        flag = 0
        for j in range(n-i):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
                flag = 1
        if(flag == 0):
            break
    return l[-2]

l = list(map(int, input("Enter the list elements: ").split()))
print("Original list : ", l)
output = secLargest(l)
print("Second Largest Element is : ", output)