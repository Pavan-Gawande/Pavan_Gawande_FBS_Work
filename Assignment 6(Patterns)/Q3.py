# Write a program to print following pattern:
#        1  
#      1   1
#    1   2   1
#  1   3   3   1

for i in range(4):
    for j in range(1, 4-i):
        print(" ", end=" ")
    
    val = 1
    for j in range(i+1):
        print(f' {val} ', end=" ")
        val = val *(i - j) // (j + 1)
    print()