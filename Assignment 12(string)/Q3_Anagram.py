# Program to Detect if Two Strings are Anagrams

def isAnagram(st1, st2):
    l1 = len(st1)
    l2 = len(st2)
    if(l2 > l1):
        st1, st2 = st2, st1
    for i in st1:
        if(st1.count(i) != st2.count(i)):
            return False
            break
    return True


st1 = input("Enter the first string: ")
st2 = input("Enter the second string : ")

if(isAnagram(st1, st2)):
    print(f"{st1} and {st2} are anagrams . . .")
else:
    print(f"{st1} and {st2} are not anagrams . . .!!")