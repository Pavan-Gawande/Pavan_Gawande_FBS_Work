# To find the root of the quadratic equation using given coefficients of equation.

a = int(input("Enter a (Coefficient of x^2) : "))
b = int(input("Enter b (Coefficient of x) : "))
c = int(input("Enter c (Constant term) : "))

root = (b*b) - (4 * a * c)  # calculate the value of discriminant(b^2 - 4ac)

if(root >= 0):   # check if discriminant is >= 0, it means roots exist. otherwise, no root exist.
    root = root**0.5
    root1 = (-b + root) / (2*a)
    root2 = (-b - root) / (2*a)
    print("Root1 : ", root1)
    print("Root2 : ", root2)

else:            # for discriminant < 0, no root exists.
    print("Root Does Not Exists.")
    