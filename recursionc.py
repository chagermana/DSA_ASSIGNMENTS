# write a program that uses a while loop to count down numbers within a range
#the user should be used to input the start and end



start = int(input("Enter the first number of your range: "))
end = int(input("Enter the ending number of your range: "))

if start<end:

    while start<=end:

        print(start)

        start= start+1

elif start>end:

    while start>=end:
        print(start)

        start=start-1

else:

    print("Start and end are equal",start)
