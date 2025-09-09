# Remove all of the vowels in a string (take input from user)

st = input("Enter the string : ")
newList = "".join([ch for ch in st if ch not in 'aAeEiIoOuU'])
print("New String : ", newList)