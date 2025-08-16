# Program to Remove the Characters of Odd Index Values in a String

def remOddIndex(st):
    output = ""
    for i in range(0, len(st), 2):
        output += st[i]
    return output

st = input("Enter the string : ")
result = remOddIndex(st)
print("Original String : ", st)
print("String after removing odd index chars : ", result)
        