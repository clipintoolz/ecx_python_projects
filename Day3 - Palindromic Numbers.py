#!/usr/bin/env python3.10

def palindrome(range_high: int) -> None:
    """prints out all palindromic numbers less than range_high provided

    Args:
        range_high (int): ranges high for palindrome search
    """

    palindrome_list = []
    for number in range(range_high):
        if str(number) == str(number)[::-1]:
            palindrome_list.append(number)

    print("Here are all palindromes less than", range_high)
    for palindromic_number in palindrome_list:
        print(palindromic_number, end=" ")


print()
print(" PALINDROME SEARCHER ".center(40, "-"))
range_high = int(
    input("Enter a number to search for palindromes in the numbers range: "))
palindrome(range_high)
