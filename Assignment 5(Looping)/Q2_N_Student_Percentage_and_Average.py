# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n = int(input("Enter the number of students: "))
max_marks = int(input("Enter the maximum marks: "))
avg_percentage = 0
for i in range(n):
    m1 = int(input(f"\nEnter marks for student {i+1} in subject 1: "))
    m2 = int(input(f"Enter marks for student {i+1} in subject 2: "))
    m3 = int(input(f"Enter marks for student {i+1} in subject 3: "))
    m4 = int(input(f"Enter marks for student {i+1} in subject 4: "))
    m5 = int(input(f"Enter marks for student {i+1} in subject 5: "))
    
    avg = ((m1 + m2 + m3 + m4 + m5) / (5 * max_marks)) * 100
    print(f"\nPercentage of student {i+1}: {avg}%")
    avg_percentage += avg

avg_percentage /= n
print(f"\nAverage percentage of all students: {avg_percentage}%")