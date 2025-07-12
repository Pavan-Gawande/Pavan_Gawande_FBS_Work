# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input("Enter marks of subject 1 : "))
sub2 = int(input("Enter marks of subject 2 : "))
sub3 = int(input("Enter marks of subject 3 : "))
sub4 = int(input("Enter marks of subject 4 : "))
sub5 = int(input("Enter marks of subject 5 : "))
max_marks = int(input("Enter maximum marks : "))
flag = 1

if( sub1 > max_marks or sub2 > max_marks or sub3 > max_marks or sub4 > max_marks or sub5 > max_marks ):
    print("Marks cannot be greater than maximum marks.")
    flag = 0
if( sub1 < 0 or sub2 < 0 or sub3 < 0 or sub4 < 0 or sub5 < 0 ):
    print("Marks cannot be negative.")
    flag = 0
if( flag ):
    per = ((sub1 + sub2 + sub3 + sub4 + sub5) / (5 * max_marks)) * 100
    if(per >= 80):
        print("First class with distinction")
    elif(per < 80 and per >= 70):
        print("First class")
    elif(per < 70 and per >= 60):
        print("Higher second class")
    elif(per < 60 and per >= 40):
        print("Second class")
    else:
        print("You are Fail")