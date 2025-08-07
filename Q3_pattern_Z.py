# program to print z pattern

for i in range(6):
    for j in range(6):
        if(i == 0 or i == 5 or j == 5-i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
