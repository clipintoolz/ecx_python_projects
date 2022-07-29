#!/usr/bin/env python3.10

def list_to_set(list_to_filter: list) -> None:
    """removes duplicate elements from a list

    Args:
        list_to_filter (list): list to remove duplicates

    Returns:
        list: filtered list
    """

    converted_list = set(list_to_filter)
    print("Filtered List: ", list(converted_list))


duplicate_list = [1, 2, 4, 5, 7, 9, 7, 5, 3, 5, 7, 8,
                  0, 6, 3, 5, 6, 9, 0, 5, 3, 3, 4, 5, 6, 7, 9, 0]
list_to_set(duplicate_list)
