# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.

divByAny = [x for x in range(1, 1001) if any(x%i == 0 for i in range(2, 10))]
print(divByAny)