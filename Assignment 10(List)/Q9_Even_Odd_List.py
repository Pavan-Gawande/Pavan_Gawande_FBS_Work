# program of having n number of elements in the list and find out even and
# odd elements in that list and then create two separate lists which will 
# have even elements and other will have odd elements.

l = list(map(int, input("Enter list elements separated by spaces : ").split()))

el = []
ol = []

for i in l : 
    if(i%2 == 0):
        el.append(i)
    else:
        ol.append(i)

print("Original list : ", l)
print("Even list : ", el)
print("Odd list : ", ol)