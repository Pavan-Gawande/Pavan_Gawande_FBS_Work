# To convert the given number of days to years, weeks and days.

Days = int(input("Enter the number of days : "))

Years = Days // 365
Days %= 365

Weeks = Days // 7
Days %= 7

print("The given number of days are equivalent to : ", Years, " Years ", Weeks, " Weeks ", Days, " Days.")