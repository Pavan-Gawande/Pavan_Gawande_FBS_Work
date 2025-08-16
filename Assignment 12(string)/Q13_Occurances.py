# Program to count the occurrences of each word in a string.

def occurances(st:str):
    unique = []
    for i in st:
        if(i not in unique):
            unique.append(i)
    for i in unique:
        print(f"{i} occurs {st.count(i)} times")

st = input("Enter the string : ")
occurances(st)