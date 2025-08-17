# Program to Add a Key-Value Pair to the Dictionary

dict1 = dict()

n = int(input("Enter the no. of key value pairs : "))
for i in range(n):
    key = input("Enter the key : ")
    value = input("Enter the value : ")
    dict1[key] = value
print("Dictionary after insertion : ", dict1)