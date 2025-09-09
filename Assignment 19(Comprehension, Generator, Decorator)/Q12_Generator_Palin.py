# Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def palindromes():
    n = 0
    while(True):
        if(str(n) == str(n)[::-1]):
            yield n
        n += 1

n = int(input("Enter no. of palindromes : "))
pal = palindromes()
for i in range(n):
    print(next(pal), end = " ")