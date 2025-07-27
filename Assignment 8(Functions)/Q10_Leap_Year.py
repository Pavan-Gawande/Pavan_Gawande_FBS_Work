# program to check if entered year is a leap year or not.

def isLeap(year):
    if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print(f"Year {year} is a leap year . . .")
    else:
        print(f"Year {year} is not a leap year . . .!!")

year = int(input("Enter the year to check if it is leap year : "))
isLeap(year)