def occurances(l):
    d = {}
    for i in l:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1
    return d

l = list(map(int, input("Enter List Elements : ").split()))
print("Original List : ", l)
output = occurances(l)
print("Final Dictionary : ", output)