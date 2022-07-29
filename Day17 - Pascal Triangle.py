#!/usr/bin/env python3.10

import math

def pascal_triangle(number_of_rows: int) -> None:
    """function that returns the first n rows of the pascal triangle

    Args:
        number_of_rows (int): first n rows
    """
    
    # for storing numbers in each row
    row_lines = []
    
    for row in range(number_of_rows):
        no_of_columns_in_each_row = row + 1
        
        # we used combination here to get the value at row(n), column(r) -> nCr
        for column in range(no_of_columns_in_each_row):
            column_value = math.comb(row, column)
            row_lines.append(str(column_value))
        
        # joins the numbers in row_lines list to form a row and then print it out
        print(" ".join(row_lines))
        
        # clears the list so a new row can be added
        row_lines.clear()
        

print()
print(" PASCAL TRIANGLE ".center(50, "-"))
number_of_rows = int(input("Enter how many rows of the pascal triangle you will like to print\n-> "))
pascal_triangle(number_of_rows)