# To convert hours,minutes and seconds to seconds.

hr = int(input("Enter the hours : "))
min = int(input("Enter the minutes : "))
sec = int(input("Enter the seconds : "))

sec += hr*3600
sec += min*60

print("Total seconds are : ", sec)