# Python program to find all the anagrams and group them together from a given list of strings.

def anaGrouping(l):
    d = {}
    for word in l:
        key = ''.join(sorted(word))
        if(key in d):
            d[key].append(word)
        else:
            d[key] = [word]
    return [d[i] for i in d]

l = list(map(str, input("Enter the list elements : ").split()))
output = anaGrouping(l)
print("Grouped anagrams : ", output)