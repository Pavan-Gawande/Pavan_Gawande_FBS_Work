# program to find factors of given number

def factors(n):
    l = []
    for i in range(1, n+1):
        if(n%i == 0):
            l.append(i)
    # print(l)
    return l

n = int(input("Enter the number : "))
facts = factors(n)
print(f'factors of {n} are ',end=" ")
for i in facts:
    print(i, end=" ")