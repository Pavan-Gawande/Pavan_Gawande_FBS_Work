# program to print given pattern:
#     10101
#     01010
#     10101
#     01010
#     10101

sym = 1
for i in range(5):
    for j in range(5):
        print(sym, end="")
        if(sym):
            sym = 0
        else:
            sym = 1
    print()