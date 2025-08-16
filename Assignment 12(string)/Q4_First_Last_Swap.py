# Program to Form a New String where the First Character and the Last Character have been Exchanged

st = input("Enter the string : ")
if(len(st) > 1):
    output = st[-1] + st[1:-1] + st[0]
else:
    output = st
print("Output string : ", output)