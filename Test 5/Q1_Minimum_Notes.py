def noteCount(n):
    d = [2000, 500, 200, 100, 50, 20, 10, 5]
    cnt = 0
    for i in d:
        cnt += n//i
        n %= i
        if(n == 0):
            return cnt

n = int(input("Enter the Amount : "))
notes = noteCount(n)
print("Minimum notes : ", notes)