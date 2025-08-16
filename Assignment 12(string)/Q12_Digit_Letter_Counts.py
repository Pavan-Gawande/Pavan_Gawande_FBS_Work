# Program to count number of digits and letters in a string.

def numLetCnt(st:str):
    digitCnt = 0
    letterCnt = 0
    for i in st:
        if(i.isdigit()):
            digitCnt += 1
        elif(i.isalpha()):
            letterCnt += 1
    return digitCnt, letterCnt

st = input("Enter the string : ")
digitCnt, letterCnt = numLetCnt(st)
print(f'{st} have {digitCnt} digits, {letterCnt} letters')