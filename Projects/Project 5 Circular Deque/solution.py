"""
CSE331 Project 5 FS'22
Circular Double-Ended Queue
solution.py
"""
from typing import TypeVar, List
from random import randint, shuffle
from timeit import default_timer
#from matplotlib import pyplot as plt  # COMMENT OUT THIS LINE (and `plot_speed`) if you dont want matplotlib
import gc

T = TypeVar('T')


class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque
        """
        if data is None and front != 0:
            data = ['Start']  # front will get set to 0 by a front enqueue if the initial data is empty
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = (self.size + front - 1) % self.capacity if data else None
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[(index + front) % capacity] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = ["CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    #
    # Your code goes here!
    #
    def __len__(self) -> int:
        """
        Returns the length(number of elements) in the deque
        :return: int representing length(number of elements) in deque
        """
        if self.front is None or self.back is None:
            return 0
        return self.size

    def is_empty(self) -> bool:
        """
        Returns a boolean indicating if the circular deque is empty
        :return: True if empty, False otherwise
        """
        return self.size == 0

    def front_element(self) -> T:
        """
        Returns the first element in the circular deque
        :return: the first element if it exists, otherwise None
        """
        if self.__len__() == 0:
            return None
        return self.queue[self.front]
    def back_element(self) -> T:
        """
        Returns the last element in the circular deque
        :return: the last element if it exists, otherwise None
        """
        if self.__len__() == 0:
            return None
        return self.queue[self.back]


    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Adds a given value to either the front or back of the circular deque based off param front
        Calls grow() if size of list has reached max capacity
        :param value: value to add into the circular deque
        :param front: If True, add to front of deque. Add to back of deque otherwise
        :return: None
        """

        if self.is_empty():
            self.front=self.back=0
            self.queue[0] = value
        elif front:
            self.front = (self.front - 1) % self.capacity
            self.queue[self.front] = value
        else:
            self.back = (self.back + 1)%self.capacity
            self.queue[self.back] = value
        self.size += 1
        if self.size==self.capacity:
            self.grow()

    def dequeue(self, front: bool = True) -> T:
        """
        Removes an item from the queue. Removes front by default, remove back if False is passed in
        Calls shrink() if current size is less than 1/4 of max capacity
        :param front: If true, remove from front of deque. Else, remove from back
        :return: Removed item, None if empty
        """
        if self.is_empty():
            return None
        if front:
            ans = self.front_element()
            self.front = (self.front + 1) % self.capacity
        else:
            ans = self.back_element()
            self.back = (self.back-1) % self.capacity
        self.size -= 1
        if self.size <= (int(self.capacity/4)):
            self.shrink()
        return ans


    def grow(self) -> None:
        """
        Doubles the capacity of a circular deque
        Unrolls old deque array into new one so front is at index 0 and back is at size-1
        :return: None
        """
        new_q = [None]*(self.capacity*2)
        i = self.front
        for j in range(self.__len__()):
            new_q[j] = self.queue[i]
            i = (i+1)%self.capacity
        self.capacity *= 2
        self.queue = new_q
        self.front = 0
        self.back = self.size - 1


    def shrink(self) -> None:
        """
        Cuts the capacity of a circular deque by 1/2 if old capacity>=8
        Unrolls old deque array into new one so front is at index 0 and back is at index size-1
        :return: None
        """
        if int((self.capacity/2)) < 4:
            return
        new_q = [None] * int((self.capacity/2))
        i = self.front
        for j in range(self.size):
            new_q[j] = self.queue[i]
            i = (i+1)%self.capacity
        self.capacity = int(self.capacity/2)
        self.queue = new_q
        self.front = 0
        self.back = self.size -1

class File:
    """
    File class stores data, used in application problem
    """
    def __init__(self, data : str) -> None:
        """
        Creates a file with data value
        :param : data , data to be stored in file
        :returns : None
        """
        self.data = data

    def __eq__(self, other: 'File') -> bool:
        """
        Compares two Files by data
        :param other: the other file
        :return: true if comparison is true, else false
        """
        return self.data == other.data

    def __str__(self) -> str:
        """
        :return: a string representation of the File
        """
        return f'File: {self.data}'

    __repr__ = __str__

def filter_corrupted(directory : List[File]) -> int:
    """
    Finds the largest list of Files without any repeats
    :param directory: list of Files to by looked through
    :return: size of the largest list of files without repeats
    """
    if len(directory) <= 1:
        return len(directory)
    longest = 0
    dict = {}
    cd = CircularDeque()
    for file in directory:
        if file.data in dict:
            dict[file.data] = 0
            cd.dequeue(front=True)
        else:
            dict[file.data] = 1
            cd.enqueue(file)
            longest = max(longest, cd.size)
    return longest







