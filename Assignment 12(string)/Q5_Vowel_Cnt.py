# Program to Count the Number of Vowels in a String

st = input("Enter the string : ")
cnt = 0
for i in st:
    if(i.isalpha() and i in "aAeEiIoOuU"):
        cnt += 1
    
print("Count of vowels : ", cnt)