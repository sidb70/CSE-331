from typing import TypeVar, Tuple  # For use in type hinting

# Type Declarations
T = TypeVar('T')  # generic type
SLL = TypeVar('SLL')  # forward declared
Node = TypeVar('Node')  # forward declare `Node` type


class SLLNode:
    """
    Node implementation
    Do not modify.
    """

    __slots__ = ['val', 'next']

    def __init__(self, value: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param value: value held by node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.val = value
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method to cast nodes to strings
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: bool
        """
        return self is other if other is not None else False


class RecursiveSinglyLinkedList:
    """
    Recursive implementation of an SLL
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        """
        return self.to_string(self.head)

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ============ Modify below ============ #

    def push(self, value: T, back: bool = True) -> None:
        """
        Pushes an SLLNode to the front or back of list, depending on param back
        :param value: value to push to the list
        :param back: Indicates whether to push node to front (False) or back (True)
        :return: None
        """
        node = SLLNode(value)
        if self.head == None:
            self.head = node
            self.tail = node
        elif back:
            self.tail.next = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node



    def to_string(self, curr: Node) -> str:
        """
        Recursively converts an SLL to a string
        :param curr: head node to start at
        :return: string representation of the linked list
        """
        if self.head == None:
            return "None"
        elif curr.next == None:
            return curr.val
        else:
            return str(curr.val + " --> " + self.to_string(curr.next))




    def length(self, curr: Node) -> int:
        """
        Recursively determines number of nodes in the list
        :param curr: head node to start at
        :return: number of nodes in list
        """
        if curr == None:
            return 0
        else:
            return 1+self.length(curr.next)



    def sum_list(self, curr: Node) -> T:
        """
        Recursively sums the values in the list
        :param curr: head node to start at
        :return: sum of values in list
        """
        if self.head == None:
            return None
        elif curr.next == None:
            return curr.val
        else:
            return curr.val + self.sum_list(curr.next)



    def search(self, value: T) -> bool:
        """
        Searches the SLL for a node containing 'value' using recursive inner function search_inner
        :param value: value to search for
        :return: result of inner function, 'True' if value is found, else 'False
        """

        def search_inner(curr: Node) -> bool:
            """
            Recursively searches SLL for node containing value
            :param curr: head node to begin the search at
            :return: 'True' if found, else 'False'
            """
            if curr == None:
                return False
            elif curr.val == value:
                return True
            else:
                return search_inner(curr.next)



        return search_inner(self.head)


    def count(self, value: T) -> int:
        """
        Returns the number of occurrences of `value` in this list using inner function count_inner
        :param value: value to count
        :return: result of count_inner, number of times the value occurred
        """

        def count_inner(curr: Node) -> int:
            """
            Recursively returns the number of occurrences of 'value' in list
            :param curr: head node to begin counting at
            :return: number of time value occurred
            """
            if curr == None:
                return 0
            else:
                return int(curr.val == value) + count_inner(curr.next)
        return count_inner(self.head)

    def remove(self, value: T) -> bool:
        """
        Removes the first node containing `value` from the SLL using recursive inner function remove_inner
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
        def remove_inner(curr: Node) -> Tuple[Node, bool]:
            """
            Recursively removes the first node containing `value` from the SLL
            :param curr: head node to begin at
            :return: Tuple containing head of list and bool that is True if a node was removed, else False
            """
            if curr== None:
                return None, False
            elif curr==self.head and curr==self.tail and curr.val == value:
                self.head = None
                self.tail = None
                return None, True
            elif curr.next == self.tail and self.tail.val == value:
                curr.next = None
                self.tail = curr
                return curr, True
            else:
                if curr.val == value:
                    return curr.next, True
                tup = remove_inner(curr.next)
                curr.next = tup[0]
                return curr, tup[1]



        return remove_inner(self.head)[1]



    def remove_all(self, value: T) -> bool:
        """
        Removes all instances of a node containing `value` from the SLL using recursive inner function remove_all_inner
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
        removed = False
        def remove_all_inner(curr: Node) -> Tuple[Node, bool]:
            """
            Recursively removes all instances of a node containing `value` from the SLL
            :param curr: head node to begin at
            :return: Tuple containing head of list and bool that is True if a node was removed, else False
            """
            nonlocal removed
            if curr == None:
                return None, removed
            elif curr == self.head and curr == self.tail and curr.val == value:
                self.head = None
                self.tail = None
                removed = True
                return None, removed
            elif curr == self.head and curr.val == value:
                self.head = curr.next
                removed = True
                return remove_all_inner(self.head), removed
            elif curr.next == self.tail and self.tail.val == value:
                curr.next = None
                self.tail = curr
                removed = True
                return curr, removed
            else:
                if curr.val == value:
                    curr = curr.next
                    removed = True
                curr.next = remove_all_inner(curr.next)[0]
                return curr, removed

        return remove_all_inner(self.head)[1]


def reverse(data: SLL, curr: Node) -> None:
    """
    Recursively reverses SLL data
    :param data: an SLL
    :param curr: head node to begin reversing at
    :return: None
    """

    if curr ==None:
        return
    if curr.next == None:
        data.head = curr
        return

    reverse(data, curr.next)
    if curr.next.next == None:
        data.tail = curr
    curr.next.next = curr
    curr.next = None




