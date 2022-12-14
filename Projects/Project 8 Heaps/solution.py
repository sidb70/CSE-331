"""
Project 8 - Heaps - Solution Code
CSE 331 Fall2022
Onsay

Sid Bhattacharya 11/17
"""

from typing import TypeVar, List

T = TypeVar('T')


class MinHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
        Returns the length of the heap
        :return: length of heap
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Checks if the heap is empty
        :return: a boolean stating if the heap is empty or not
        """
        return len(self.data)==0

    def top(self) -> T:
        """
        Returns the top (minimum) value of the MinHeap
        :return: top (minimum) value in the MinHeap
        """
        if not self.empty():
            return self.data[0]

    def get_left_child_index(self, index: int) -> int:
        """
        Computes the index of the left child at the parent index
        :param index: parent index from which the left child is being calculated
        :return: an int with the left child's index (or None if no such child exists)
        """
        if (2*index)+1 < len(self.data):
            return (2*index) + 1
        return None

    def get_right_child_index(self, index: int) -> int:
        """
        Computes the index of the right child at the parent index
        :param index: parent index from which the right child is being calculated
        :return: an int with the right child's index (or None if no such child exists)
        """
        if (2*index)+2 < len(self.data):
            return (2*index) + 2
        return None

    def get_parent_index(self, index: int) -> int:
        """
        Computes the index of the parent at the child index
        :param index: child index from which the parent is being calculated
        :return: an int with the parent's index (or None if no such parent exists)
        """
        if index==0:
            return None
        return (index-1)//2

    def get_min_child_index(self, index: int) -> int:
        """
        Computes the index of the child with the lower value at the parent index
        :param index: parent index from which min child is being computed
        :return: an int with the minimum value child's index (or None if no children)
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        if left is None or right is None:
            if not left:
                return right
            return left
        elif self.data[left] < self.data[right]:
            return left
        return right

    def percolate_up(self, index: int) -> None:
        """
        Percolates up the value at index to its valid spot in the heap
        :param index: index to begin percolation up
        :return: None
        """
        parent = self.get_parent_index(index)
        if parent is not None and self.data[index]<self.data[parent]:
            self.data[index],self.data[parent] = self.data[parent],self.data[index]
            self.percolate_up(parent)

    def percolate_down(self, index: int) -> None:
        """
        Percolates down the value at index to its valid spot in the heap
        :param index: index to begin percolation down
        :return: None
        """
        min_child_ind = self.get_min_child_index(index)
        if min_child_ind is not None and self.data[min_child_ind]<self.data[index]:
            self.data[index], self.data[min_child_ind] = self.data[min_child_ind], self.data[index]
            self.percolate_down(min_child_ind)

    def push(self, val: T) -> None:
        """
        Adds a new element to the heap
        :param val: value of the new element
        :return: None
        """
        self.data.append(val)
        self.percolate_up(len(self.data)-1)

    def pop(self) -> T:
        """
        Removes the smallest element from the heap
        :return: the top of the heap
        """
        if not self.empty():
            ret = self.top()
            self.data[0] = self.data[len(self.data)-1]
            self.data.pop()
            self.percolate_down(0)
            return ret


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = MinHeap()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    __repr__ = __str__

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.to_tree_format_string()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
        Checks if the heap is empty
        :return: a boolean stating if the heap is empty or not
        """
        return len(self.data) == 0

    def top(self) -> int:
        """
        Returns the top (maximum) value of the MinHeap
        :return: top (maximum) value in the MinHeap
        """
        if not self.empty():
            return 0-self.data.top()

    def push(self, key: int) -> None:
        """
        Adds a new element to the heap
        :param val: value of the new element
        :return: None
        """
        self.data.push(0-key)

    def pop(self) -> int:
        """
        Removes the largest element from the heap
        :return: the top of the heap
        """
        return 0-self.data.pop()


def get_eating_times(values: List[List[List[int]]]) -> List[List[int]]:
    """
    Finds available eating times in the form of finite-length intervals that do not overlap with any of the given intervals, in sorted order
    :param values: List of intervals for each family member during which they will be in the vicinity of the turkey
    :return: A list of non overlapping intervals during which we can eat the turkey
    """
    if len(values) == 0:
        return []
    start_times = MinHeap()
    end_times = MinHeap()

    for member in values:
        for interval in member:
            start_times.push(interval[0])
            end_times.push(interval[1])

    available = []

    prev = [start_times.pop(), end_times.pop()]
    while not start_times.empty() and not end_times.empty():
        curr = [start_times.pop(), end_times.pop()]
        if curr[0] <= prev[1]:
            prev[1] = curr[1]
        elif curr[0] > prev[1]:
            available.append([prev[1], curr[0]])
            prev = curr
    return available

