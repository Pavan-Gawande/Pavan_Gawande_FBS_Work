# Program to count number of lowercase characters in a string.

def numLower(st):
    cnt = 0
    for i in st:
        if(i.islower()):
            cnt += 1
    return cnt

st = input("Enter the string : ")
print(f"{st} have {numLower(st)} lowercase letters")