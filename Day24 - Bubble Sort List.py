#!/usr/bin/env python3.10

def bubble_sort(list_to_sort: list, reverse: bool = False) -> None:
    """sorts element in a list in ascending or descending order

    Args:
        list_to_sort (list): list to sort
        reverse (bool, optional): set reverse = True to sort in descending order. Defaults to False.
    """
    
    # number of elements in list
    length_of_list = len(list_to_sort)
    
    # this will enable us repeat the swapping process till list is sorted
    for _ in range(length_of_list):
        
        for index in range(length_of_list):
            
            # checks if current element is the last element in the list
            if list_to_sort[index] != list_to_sort[length_of_list - 1]:
                
                # checks if current element is less than previous elements, if true, swap their positions
                if list_to_sort[index] > list_to_sort[index + 1]:
                    x, y = list_to_sort[index], list_to_sort[index + 1]
                    list_to_sort[index], list_to_sort[index + 1] = y, x
    
    # prints list in ascending order                
    if not reverse:
        print(list_to_sort)
    
    # prints list in descending order   
    else:
        list_to_sort.reverse()
        print(list_to_sort)
    

bubble_sort([2, 4, 1, 9, 6, 8, 7, 3, 12, 22, 15, 14, 17], reverse=True)
