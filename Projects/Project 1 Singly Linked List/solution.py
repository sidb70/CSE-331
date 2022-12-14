from typing import TypeVar  # For use in type hinting

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
        # return self.val == other.val if other is not None else False


class SinglyLinkedList:
    """
    Implementation of an SLL
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ============ Modify below ============ #
    def push(self, value: T) -> None:
        """
        Pushes an SLLNode to the end of the list
        :param value: value to push to the list
        :return: None
        """
        node = SLLNode(value)
        node.next = None
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

# WRITE YOUR CODE HERE
    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of the linked list
        """
        curr = self.head
        if curr==None:
            return "None"
        to_str = ""
        while(curr.next != None):
            to_str += str(curr.val) + " --> "
            curr = curr.next
        return to_str + str(curr.val)


# WRITE YOUR CODE HERE

    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        # WRITE YOUR CODE HERE
        if(self.head == None):
            return 0
        length = 1
        curr = self.head
        while(curr.next != None):
            length += 1
            curr = curr.next
        return length

    def sum_list(self) -> T:
        """
        Sums the values in the list
        :return: sum of values in list
        """
        # WRITE YOUR CODE HERE
        if(self.head == None):
            return None
        sum = self.head.val
        curr = self.head
        while(curr.next != None):
            curr = curr.next
            sum += curr.val
        return sum


    def remove(self, value: T) -> bool:
        """
        Removes the first node containing `value` from the SLL
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
        # WRITE YOUR CODE HERE
        if(self.head == None):
            return False
        prev = None
        curr = self.head
        while(curr):
            if(curr.val == value):
                if (prev!=None):
                    prev.next = curr.next
                    if(prev.next == None):
                        self.tail = prev
                else:
                    self.head = curr.next
                    if self.head == None:
                        self.tail = None
                return True
            prev = curr
            curr = curr.next
        return False



    def remove_all(self, value: T) -> bool:
        """
        Removes all instances of a node containing `value` from the SLL
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
# WRITE YOUR CODE HERE
        prev = None
        curr = self.head
        removed = False
        while(curr):
            if(curr.val == value):
                if(prev!= None):
                    prev.next = curr.next
                    if(prev.next == None):
                        self.tail = prev
                    elif(curr==self.head):
                        self.head=curr.next
                else:
                    self.head = curr.next
                    if(self.head == None):
                        self.tail = None
                removed = True
            prev = curr
            curr = curr.next
        return removed
    def search(self, value: T) -> bool:
        """
        Searches the SLL for a node containing `value`
        :param value: value to search for
        :return: `True` if found, else `False`
        """
# WRITE YOUR CODE HERE
        curr = self.head
        while curr:
            if(curr.val == value):
                return True
            curr = curr.next
        return False

    def count(self, value: T) -> int:
        """
        Returns the number of occurrences of `value` in this list
        :param value: value to count
        :return: number of times the value occurred
        """
# WRITE YOUR CODE HERE
        total =0
        curr = self.head
        while curr:
            if curr.val == value:
                total +=1
            curr = curr.next
        return total


def reverse(data: SLL) -> None:
    """
    Reverses the data
    :param data: an SLL
    :return: None
    """
# WRITE YOUR CODE HERE
    curr = data.head
    data.head = data.tail
    data.tail = curr

    prev = None
    while (curr):
        next =curr.next
        curr.next = prev
        prev= curr
        curr = next

    data.head = prev

