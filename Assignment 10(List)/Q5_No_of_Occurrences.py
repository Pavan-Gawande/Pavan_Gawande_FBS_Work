# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

n = int(input("Enter the no. of element : "))
l = []
for i in range(n):
    l.append(int(input()))

cnt = 0
ele = int(input("Enter the element to find : "))
for i in range(n):
    if(l[i] == ele):
        cnt += 1
    
if(cnt):
    print(f"{ele} occurs {cnt} times in list ")
else:
    print(f"{ele} does not found in the given list")