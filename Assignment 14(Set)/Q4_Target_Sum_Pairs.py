# Python program that finds all pairs of elements in a list whose sum is equal to a given value.

def summingPairs(l, target):
    final = set()
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if(l[i]+l[j] == target):
                final.add((l[i], l[j]))
    return final

l = list(map(int, input("Enter the list elements : ").split()))
target = int(input("Enter the target sum : "))
output = summingPairs(l, target)
print("Target sum pairs are : ", output)