#!/usr/bin/env python3.10

def magic_square_validator(list_to_validate: list[list]) -> None:
    """checks to see if a list of numbers make up a magic square

    Args:
        list_to_validate (list[list]): list of list containing numbers in each horizontal row
    """

    # checks if the list contains more than 3 nested list
    if len(list_to_validate) > 3:
        print("List should not cointain more than 3 nested list")

    # checks if the list does not contain up to 3 nested list
    elif len(list_to_validate) < 3:
        print("List should cointain 3 nested list")


    elif len(list_to_validate) == 3:
        
        # seperates each list into list_1 to list_3 variables
        list_1 = list_to_validate[0]
        list_2 = list_to_validate[1]
        list_3 = list_to_validate[2]

        # checks if the nested list contains more than 3 numbers
        if len(list_1) > 3 or len(list_2) > 3 or len(list_3) > 3:
            print("Nested list should not cointain more than 3 numbers")

        # checks if the nested list does not contains up to 3 numbers
        elif len(list_1) < 3 or len(list_2) < 3 or len(list_3) < 3:
            print("Nested list should cointain 3 numbers")

        # checks if the nested list contains exactly 3 numbers
        elif len(list_1) == 3 and len(list_2) == 3 and len(list_3) == 3:
            
            # checks if the numbers in the nested list are between 1 to 9
            list_1_check = bool(min(list_1) >= 1 and max(list_1) <= 9)
            list_2_check = bool(min(list_2) >= 1 and max(list_2) <= 9)
            list_3_check = bool(min(list_3) >= 1 and max(list_3) <= 9)
            
            if list_1_check and list_2_check and list_3_check:
                
                # sum of rows
                row_1_sum = sum(list_1)
                row_2_sum = sum(list_2)
                row_3_sum = sum(list_3)
                
                # sum of columns 
                column_1_sum = (list_1[0] + list_2[0] + list_3[0])
                column_2_sum = (list_1[1] + list_2[1] + list_3[1])
                column_3_sum = (list_1[2] + list_2[2] + list_3[2])
                
                # sum of right diagonal
                left_diagonal_sum = (list_1[0] + list_2[1] + list_3[2])
                
                # sum of left diagonal
                right_diagonal_sum = (list_1[2] + list_2[1] + list_3[0])

                # checks if the sum of each row, column and diagonals are equal
                magic_square_check = row_1_sum == row_2_sum == row_3_sum == column_1_sum == column_2_sum == column_3_sum == left_diagonal_sum == right_diagonal_sum

                # checks if the sum of each row, column and diagonals are equal
                if magic_square_check:
                    print()
                    print("It's a magic square")
                    print(*list_1, sep=" | ")
                    print(*list_2, sep=" | ")
                    print(*list_3, sep=" | ")
                else:
                    print()
                    print("Not a magic square")
                    print(*list_1, sep=" | ")
                    print(*list_2, sep=" | ")
                    print(*list_3, sep=" | ")

            else:
                print("Numbers in list must be between 1 and 9")


number = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
magic_square_validator(number)
