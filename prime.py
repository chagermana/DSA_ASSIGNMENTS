# write a recursive function that determines whether a given number is a prime number by checking for divisibility integers less than n\

def is_prime_recursive(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

# Example usage:
num = int(input("Enter a number to check if it's prime: "))
if is_prime_recursive(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
