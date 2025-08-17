# Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

def numSum3(l, target):
    triplets = set()
    n = len(l)
    i, j, k = 0, 1, 2
    while(i < n-2):
        # print(i, j, k)
        if((l[i]+l[j]+l[k]) == target):
            temp = [l[i], l[j], l[k]]
            triplets.add(tuple(sorted(temp)))
        k += 1
        if(k == n):
            j += 1
            if(j == n-1):
                i += 1
                j = i + 1
            k = j + 1
    return triplets

l = list(map(int, input("Enter the list elements : ").split()))
target = int(input("Enter the target sum : "))
output = numSum3(l, target)
print("Target sum pairs are : ", output)