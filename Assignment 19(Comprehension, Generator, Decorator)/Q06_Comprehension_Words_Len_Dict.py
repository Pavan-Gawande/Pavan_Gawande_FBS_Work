# Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

s = input("Enter the strings : ")
wordDict = {word : len(word) for word in s.split()}
print(wordDict)