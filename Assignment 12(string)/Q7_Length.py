# Program to Calculate the Length of a String Without Using a Library Function

def length(st):
    cnt = 0
    for i in st:
        cnt += 1
    return cnt

st = input("Enter the string : ")
size = length(st)
print(f"Length of {st} is {size}")