# PLEASE NOTE : method must call itself and the method should call itself

# write  a recursive function that takes 2 integers as input and returns their product using repeated addition without using multiplication operator


def product(a , b):

    if b == 0:
        return 0

    elif b > 0:
        return a + product(a,b-1)

    else:
        return -product(a,-b)

print(product(2,3))



