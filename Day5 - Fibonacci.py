#!/usr/bin/env python3.10

# Define fibonacci formula
def fibonacci(number: int) -> int:
    """determines the value of the nth term of a fibonacci sequence

    Args:
        number (int): nth term of fibonacci sequence

    Returns:
        int: fibonacci value
    """

    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print()
print(" FIBONACCI SERIES ".center(30, "-"))
number_of_sequence = int(
    input("Enter number of fibonacci sequence to return: "))

# Prints each element of fibonacci sequence on a single line
if number_of_sequence <= 0:
    print("Invalid Number")
else:
    for i in range(number_of_sequence):
        print(fibonacci(i), end="  ")
