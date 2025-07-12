# program to calculate profit or loss.

buy_price = int(input("Enter the buying price : "))
sell_price = int(input("Enter the selling price : "))

diff = sell_price - buy_price

if(diff > 0):
    print("You made profit of : Rs.", diff)
elif(diff < 0):
    print("You made loss of : Rs.", -(diff))
else:
    print("You didn't made any profit or loss...")