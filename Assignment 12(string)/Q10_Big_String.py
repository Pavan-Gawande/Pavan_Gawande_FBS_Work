# Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

def length(st):
    cnt = 0
    for i in st:
        cnt += 1
    return cnt

st1 = input("Enter String1 : ")
st2 = input("Enter String2 : ")

if(length(st1) > length(st2)):
    print(f"{st1} is bigger string")
else:
    print(f"{st2} is bigger string")