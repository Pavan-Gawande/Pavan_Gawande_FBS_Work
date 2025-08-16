# Program to Calculate the Number of Words and the Number of Characters Present in a String

def cwCount(st):
    charCnt = 0
    wordCnt = 0
    l = st.split()
    for i in l:
        if(not i.isspace()):
            wordCnt += 1
            charCnt += len(i)
    return charCnt, wordCnt
    
    

st = input("Enter the string : ")
charCnt, wordCnt = cwCount(st)
print("Original String : ", st)
print(f'above string contains {wordCnt} words, {charCnt} characters.')