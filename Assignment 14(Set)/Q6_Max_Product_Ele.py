# Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

def maxProd(l):
    mxpro = 0
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if(l[i]*l[j] > mxpro):
                mxpro = l[i]*l[j]
                mxSet = {l[i], l[j]}
    return mxSet

l = list(map(int, input("Enter the list elements : ").split()))
output = maxProd(l)
print("Original List : ", l)
print("Max Product Elements ", output)