#!/usr/bin/env python3.10

def is_prime(number: int):
    """determines whether a number is a prime number or not

    Args:
        number (int): number to check
    """
    
    # Negative numbers and 1 are not prime numbers
    if number <= 1:
        print(f"{number} is not a prime number")
        
    else:
        # checks if the number is divisible by any integer less than the number to check, if it's divisible then it's not a prime number
        for divisor in range(2, number):
            is_prime = True
            if number % divisor == 0:
                is_prime = False
                break
            
    if is_prime == True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

print()
print(" PRIME NUMBER CHECKER ".center(50, "-"))
number = int(input("Enter number to check: "))
is_prime(number)