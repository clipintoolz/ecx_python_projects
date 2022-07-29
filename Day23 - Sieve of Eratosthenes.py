#!/usr/bin/env python3.10

def prime_list(range_of_numbers: int) -> None:
    """prints out the list of prime numbers between a range of numbers

    Args:
        range_of_numbers (int): range to check for prime numbers
    """

    # to store the prime numbers
    prime_numbers_list = []
    
    # negative numbers and 1 are not prime numbers
    if range_of_numbers <= 1:
        print(f"No primes found between 0 and {range_of_numbers}")
        
    else:
        # checks if each number number in the range is divisible by any integer less than the number to check, if it's divisible then it's not a prime number
        for number in range(2, range_of_numbers + 1):
            is_prime = True
            for divisor in range(2, number):
                if number % divisor == 0:
                    is_prime = False
                    break
            
            # if the number was not divisible by any integer less than the number then add it to the prime_numbers_list
            if is_prime == True:
                prime_numbers_list.append(number)

        print(prime_numbers_list)


print()
print(" PRIME NUMBERS LIST".center(50, "-"))
print("Find all prime numbers below a certain number using sieve of eratosthenes")
user_input = int(input("Enter Number\n-> "))
prime_list(user_input)
