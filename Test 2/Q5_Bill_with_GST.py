# To calculate the total cost of 5 products including GST

prod1 = int(input("Enter the price of product 1: "))
prod2 = int(input("Enter the price of product 2: "))
prod3 = int(input("Enter the price of product 3: "))
prod4 = int(input("Enter the price of product 4: "))
prod5 = int(input("Enter the price of product 5: "))

total_cost = prod1 + prod2 + prod3 + prod4 + prod5
total_cost += total_cost * 0.18                                                     # Adding 18% GST`
print("Total cost of the products including GST is: Rs.", total_cost)