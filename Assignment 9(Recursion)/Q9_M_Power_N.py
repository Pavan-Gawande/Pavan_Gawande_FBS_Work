# program to calculate the m to the power n using recursion.

def powMN(m, n):
    if(n == 0):
        return 1
    elif(n > 0):
        return m * powMN(m, n-1)
    else:
        return (1/m) * powMN(m, n+1)

M = int(input("Enter the value of M(Base) : "))
N = int(input("Enter the value of N(Exponent) : "))

print(f"Value of {M}^{N} is {powMN(M, N)}")