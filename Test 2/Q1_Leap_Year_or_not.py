# To find the given year is leap year or not

year = int(input("Enter the year : "))
if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("Given year is a leap year...")
        else:
            print("Given year is not a leap year...!!")
    else:
        print("Given year is a leap year...")
else:
    print("Given year is not a leap year...!!")