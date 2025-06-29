# To find the selling price based on given cost price and discount

CostPrice = int(input("Enter the cost price of the book : "))
Discount = int(input("Enter the discount rate(in Percent) : "))


SellPrice = CostPrice*((100 - Discount)/ 100)

print("The Selling Price Would be : ", SellPrice)
