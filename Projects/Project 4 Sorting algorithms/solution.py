"""
Project 4 - Hybrid Sorting - Solution Code
CSE 331 Fall 2022
"""

import gc
import random
import time
from typing import TypeVar, List, Callable, Dict

T = TypeVar("T")  # represents generic type


# do_comparison is an optional helper function but HIGHLY recommended!!!
def do_comparison(first: T, second: T, key: Callable[[T], T], descending: bool) -> bool:
    """
    Compares two elements based on given key
    :param first: the first element in comparison
    :param second: the second element in comparison
    :param key: A function which takes an argument of type T and returns new value of first argument
    :param descending: determines whether elements should be compares ascending or descending
    :return: true if first element (if !descending) or second element (if descending) is greater than other
    """
    if descending:
        return key(first) < key(second)
    return key(first) > key(second)

def selection_sort(data: List[T], *, key: Callable[[T], T] = lambda x: x,
                   descending: bool = False) -> None:
    """
    In-place implementation of selection sort
    :param data: list to be sorted
    :param key: A function which takes an argument of type T and returns new value of first argument
    :param descending: perform sort in descending order when True. Default is False
    :return: None
    """
    for i in range(len(data)):
        min_element = i
        for j in range(i+1, len(data)):
            if do_comparison(data[min_element], data[j], key, descending):
                min_element = j
        temp = data[i]
        data[i] = data[min_element]
        data[min_element] = temp


def bubble_sort(data: List[T], *, key: Callable[[T], T] = lambda x: x,
                descending: bool = False) -> None:
    """
    In-place implementation of bubble sort
    :param data: list to be sorted
    :param key: A function which takes an argument of type T and returns new value of first argument
    :param descending: perform sort in descending order when True. Default is False
    :return: None
    """
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if do_comparison(data[j], data[j+1], key, descending):
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

def insertion_sort(data: List[T], *, key: Callable[[T], T] = lambda x: x,
                   descending: bool = False) -> None:
    """
    In-place implementation of insertion sort
    :param data: list to be sorted
    :param key: A function which takes an argument of type T and returns new value of first argument
    :param descending: perform sort in descending order when True. Default is False
    :return: None
    """
    for i in range(1, len(data)):
        curr = data[i]
        j = i
        while j > 0 and do_comparison(data[j-1], curr, key, descending):
            data[j] = data[j-1]
            j -= 1
        data[j] = curr


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      key: Callable[[T], T] = lambda x: x, descending: bool = False) -> None:
    """
    Hybrid merge sort implementation that uses merge sort and insertion sort
    :param data: list to be sorted
    :param threshold: list size threshold at or under which insertion sort is to be used
    :param key: A function which takes an argument of type T and returns new value of first argument
    :param descending: perform sort in descending order when True. Default is False
    :return: None
    """
    def merge(left: List[T],right: List[T], *,key: Callable[[T], T] = lambda x: x,
                                            descending: bool = False) -> None:
        """
        Inner function used to merge two sorted arrays during merge process
        :param left: first sorted list
        :param right: second sorted list
        :param key: A function which takes an argument of type T and returns new value of first argument
        :param descending: perform sort in descending order when True. Default is False
        :return None:
        """
        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if do_comparison(right[j], left[i], key, descending):
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i<len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            data[k] = right[j]
            j += 1
            k += 1
    if len(data)<=threshold+1:
        insertion_sort(data, key=key, descending=descending)
    else:
        mid = int(len(data)/2)
        left = data[:mid]
        right = data[mid:]
        hybrid_merge_sort(left, threshold=threshold, key=key, descending=descending)
        hybrid_merge_sort(right, threshold=threshold, key=key, descending=descending)
        merge(left, right, key=key, descending=descending)



# A hybrid quicksort would be even faster, but we don't want to give too much code away here!
def quicksort(data):
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first, last):
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


def sort_sushi(sushi: List[str], key: Callable[[T], T] = lambda x: {'D': 0, 'A': 1, 'C': 2}[x]) -> None:
    """
    Sorts sushi rolls in-place such that all the sushi rolls of the same type are
    together and that the sushi types appear order specified by key dictionary
    :param sushi: list of sushi string characters to sort
    :param key: A function which takes an argument of type T and returns new value of first argument
    :return: None
    """
    num0 = 0
    num1 = 0
    num2 = 0
    roll0 = 'D'
    roll1 = 'A'
    roll2 = 'C'
    for s in sushi:
        if key(s) == 0:
            num0 += 1
            roll0 = s
        elif key(s) == 1:
            num1 += 1
            roll1 = s
        elif key(s) == 2:
            num2 += 1
            roll2 = s
    if num0>0:
        sushi[:num0] = [roll0]*num0
    if num1>0:
        sushi[num0:num0+num1] = [roll1]*num1
    if num2>0:
        sushi[num0+num1:] = [roll2]*num2

