# program to reverse the list.

n = int(input("Enter the no. of element : "))
l = []
for i in range(n):
    l.append(int(input()))

print("Original List : ",l)

for i in range(n//2):
    l[i], l[n-1-i] = l[n-1-i], l[i]

print("Reverse List : ", l)