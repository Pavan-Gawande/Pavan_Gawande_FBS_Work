# To find the simple interest using given values of P, R, T

P = float(input("Enter the principal amount : "))
R = float(input("Enter the rate of interest (Per Year) : "))
T = float(input("Enter the time duration (In months) : "))

T /= 12                             # Time converted into years

SI = (P*R*T) / 100

print("The Simple Interest is : ",SI)