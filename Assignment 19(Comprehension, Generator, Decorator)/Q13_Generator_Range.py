# Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def custRange(start, stop=None, step = 1):
    if(stop == None):
        start, stop = 0, start
    if(step > 0):
        while(start < stop):
            yield start
            start += step
    else:
        while(start > stop):
            yield start
            start += step

for i in custRange(2, 20, 2):
    print(i)