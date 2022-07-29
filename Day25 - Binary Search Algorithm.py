#!/usr/bin/env python3.10


def binary_search(list_to_search: list, value: int | float, start_index: int, stop_index: int) -> int:
    """_summary_

    Args:
        list_to_search (list): _description_
        value (int | float): value to get index
        start_index (int): initialy always zero
        stop_index (int): index of the last element

    Returns:
       int: index of value
    """
    sorted_list = sorted(list_to_search)

    if list_to_search != sorted_list:
        print("List is not sorted")

    else:
        # return -1 instead of raising an exception
        if start_index > stop_index:
            return -1
        
        middle_index = (start_index + stop_index) // 2

        if value < list_to_search[middle_index]:
            return binary_search(list_to_search, value, start_index, middle_index - 1)
        
        elif value > list_to_search[middle_index]:
            return binary_search(list_to_search, value, middle_index + 1, stop_index)
        
        elif value == list_to_search[middle_index]:
            return middle_index


num_list = [1,2,3,4,5,6,7,8,9]
print(binary_search(num_list, 1, 0, len(num_list) - 1))
