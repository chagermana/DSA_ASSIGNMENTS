# write a program that uses a while loop to count down numbers within a range
#the user should be used to input the start and end but RECURSION
from itertools import count

#from recursion1b import countdown


def countdown(start,end):

    print(end)

    if end == start: #base case
        return

    else:
        countdown(start,end-1) #general case

countdown(10,20)


