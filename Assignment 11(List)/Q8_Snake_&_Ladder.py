# Program to print 1 to 100 in snakes and ladder pattern.

def snakeLadder():
    main = []
    for i in range(10, 0, -1):
        temp = []
        for j in range(10):
            temp.append(10*i - j)
        if(i%2 == 1):
            temp.reverse()
        main.append(temp)
    for i in main:
        print(i)

snakeLadder()
    