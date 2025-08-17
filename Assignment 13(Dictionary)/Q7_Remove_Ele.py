# Program to Remove the Given Key from a Dictionary
 
d = {'name':'pavan', 'age': 21, 'lang':'Python', 'extra':1234}
print('Original Dictionary : ', d)
key = input("Enter the key to remove : ")
d.pop(key)
print("Dictionary after Removal : ",d)
