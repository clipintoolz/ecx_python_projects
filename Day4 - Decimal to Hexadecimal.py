#!/usr/bin/env python3.10

def decimal_to_hex(number: int) -> None:
    """converts a base 10 number to base 16(hex)

    Args:
        number (int): base 10 number to convert
    """

    hex_number_list = []
    quotient = number

    # Hexadecimal Representation
    to_hex = {10: "a",
              11: "b",
              12: "c",
              13: "d",
              14: "e",
              15: "f"}

    # Appends each remainder to hex_number_list while the quotients is greater than 16
    while quotient > 16:
        dividend = quotient
        quotient, remainder = divmod(dividend, 16)

        if remainder == 10:
            hex_number_list.append("a")
        elif remainder == 11:
            hex_number_list.append("b")
        elif remainder == 12:
            hex_number_list.append("c")
        elif remainder == 13:
            hex_number_list.append("d")
        elif remainder == 14:
            hex_number_list.append("e")
        elif remainder == 15:
            hex_number_list.append("f")
        else:
            hex_number_list.append(str(remainder))

    # Appends the last quotient converted to hex if it's less than 16
    if quotient in to_hex.keys():
        hex_number_list.append(to_hex[quotient])
    else:
        hex_number_list.append(str(quotient))

    # Joins all remainders with the last quotient in reverse order
    hex_number = "0x" + "".join(hex_number_list[::-1])
    print(f"Hexadecimal representation of {number} is {hex_number}")


print()
print(" DECIMAL TO HEXADECIMAL CONVERTER ".center(50, "-"))
number_to_convert = int(input("Enter a number to convert to hexadecimal: "))
decimal_to_hex(number_to_convert)
