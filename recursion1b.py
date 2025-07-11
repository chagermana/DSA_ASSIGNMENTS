#write a python program that achieve the same as q1 ie as a recursive method that counts down from n to 1

def countdown(n):

    print(n)

    if n == 1:
        return

    else:
        countdown(n - 1)#method must call itself
countdown(10)

# def countdown(n):
#     if n >= 1:
#         print(n)
#         countdown(n - 1)
#
# # Get user input and call the function
# n = int(input("Enter a number: "))
# countdown(n)








