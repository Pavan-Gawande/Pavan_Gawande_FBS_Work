# Program to Multiply All the Items in a Dictionary

def sumEle(d):
    total = 1
    for i in d:
        total *= d[i]
    return {'total' : total}

dict1 = dict()
n = int(input("Enter the no. of key value pairs : "))
for i in range(n):
    key = input("Enter the key : ")
    value = int(input("Enter the value : "))
    dict1[key] = value

print(f'Original Dictionary : ', dict1)
total = sumEle(dict1)
print(f'Final Dictionary : ', total)