# Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

def occurances(st):
    s = set()
    for i in st:
        s.add(i)
    for i in s:
        print(f'{i} occurs {st.count(i)}')

st = input("Enter the string : ")
occurances(st)