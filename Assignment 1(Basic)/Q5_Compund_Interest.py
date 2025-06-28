# To find the compound interest

P = int(input("Enter the principal Amount : "))
R = float(input("Enter the rate of Interest : "))
T = int(input("Enter the time (in months) : "))
N = int(input("ENter the no. of time interest is compounded in a year (eg. 4 for Quaterly) : "))

T /= 12                         # Time converted into years
R /= 100                        # Interest rate converted into decimal

Amount = P * ( (1 + (R/N) )**(N*T) )

CI = Amount - P                 # Cmpound interest calculated by reducing the principal from total amount

print("The Compound Interest will be : ", CI)