#!/usr/bin/python3
"""Finding the peak of alist of unsorted integers"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers using binary search.

    Parameters:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak element if found, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
