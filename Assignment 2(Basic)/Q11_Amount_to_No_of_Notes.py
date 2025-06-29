# To find the minimum number of notes needed to make given amount

amount = int(input("Enter the amount : "))

n500 = amount // 500
amount %= 500

n200 = amount // 200
amount %= 200

n100 = amount // 100
amount %= 100

n50 = amount // 50
amount %= 50

n20 = amount // 20
amount %= 20

n10 = amount // 10
amount %= 10

print("Notes needed to make the given amount : \n",
      n500," ₹500 notes\n",
      n200," ₹200 notes\n",
      n100," ₹100 notes\n",
      n50," ₹50 notes\n",
      n20," ₹20 notes\n",
      n10," ₹10 notes\n")