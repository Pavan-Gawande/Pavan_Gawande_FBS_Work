# Program to Concatenate Two Dictionaries Into One

def mergeDictionary(d1, d2):
    merged = d1.copy()
    for i in d2:
        merged[i] = d2[i]
    return merged
    
dict1 = {'name': 'Pavan', 'age': 21}
dict2 = {'progLang':'Python'}

print('Dictionary 1 : ', dict1)
print("Dictionary 2 : ", dict2)

merged = mergeDictionary(dict1, dict2)

print("Merged Dictionary : ", merged)