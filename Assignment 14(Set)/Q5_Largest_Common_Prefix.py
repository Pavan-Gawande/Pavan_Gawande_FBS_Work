# Python program to find the longest common prefix of all strings. Use the Python set.

def longestCommonPrefix(l):
    pre = l[0]
    for i in l[1:]:
        end = 0
        for j in range(min(len(i), len(pre))):
            if(i[j] == pre[j]):
                end += 1
        pre = pre[:end]
    return pre

l = list(map(str, input("Enter the list elements : ").split()))
prefix = longestCommonPrefix(l)
print('The largest common prefix is ',prefix)