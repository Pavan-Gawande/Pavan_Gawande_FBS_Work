def missCoin(l):
    d = {}
    for i in l:
        if(i in d):
            d[i] += 1
        else:
            d[i] = 1
    for key in d:
        if(d[key]%2 == 1):
            return key

n = int(input("Enter no. of coins : "))
l = list(map(int, input("Enter the number on each coin : ").split()))
coin = missCoin(l)
print("Coins : ", l)
print("Missing Coin : ", coin)
        