# program to input any alphabet and check whether it is vowel or consonant.

alpha = input("Enter a character : ")
if(alpha in "aeiou" or alpha in "AEIOU"):
    print("Given alphabet is Vowel...")
else:
    print("Given alphabet is Consonant")