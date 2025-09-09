# Find all of the words in a string that are less than 5 letters (take input from user)

st = input("Enter the string : ")
wordLenLess5 = [word for word in st.split() if len(word) < 5]
print("Words Length Less than 5 are : ", wordLenLess5)