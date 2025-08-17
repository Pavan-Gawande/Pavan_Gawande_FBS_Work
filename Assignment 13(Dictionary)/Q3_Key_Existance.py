# Program to Check if a Given Key Exists in a Dictionary or Not

def existance(dict, target):
    for i in dict:
        if(i == target):
            return True
    return False

dict1 = {'name': 'Pavan', 'age': 21, 'progLang': 'Python'}
target = input("Enter the key : ")
if(existance(dict1, target)):
    print(f'{target} is present in dictionary. ')
else:
    print(f'{target} is not present in dictionary. ')
    