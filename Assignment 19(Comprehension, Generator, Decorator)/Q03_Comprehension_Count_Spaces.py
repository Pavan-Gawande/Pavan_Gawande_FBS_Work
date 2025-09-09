# Count the number of spaces in a string (take input from user)

st = input("Enter the string : ")

count = sum([1 for i in st if i==" "])
print("Total Counts of spaces is : ", count)