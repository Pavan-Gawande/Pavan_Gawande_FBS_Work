# Program to Count the Frequency of Words Appearing in a String Using a Dictionary

def occurance(st):
    d = dict()
    for i in st:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1
    return d
    
st = input("Enter the string : ")
output = occurance(st)
for i in output:
    print(f'{i} occurs {output[i]} times')