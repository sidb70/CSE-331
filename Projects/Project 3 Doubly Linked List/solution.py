
from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    def __eq__(self, other: Node):
        return self.value == other.value

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
            if node is self.head:
                break
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    def __eq__(self, other: DLL) -> bool:
        """
        :param other: compares equality with this List
        :return: True if equal otherwise False
        """
        cur_node = self.head
        other_node = other.head
        while True:
            if cur_node != other_node:
                return False
            if cur_node is None and other_node is None:
                return True
            if cur_node is None or other_node is None:
                return False
            cur_node = cur_node.next
            other_node = other_node.next
            if cur_node is self.head and other_node is other.head:
                return True
            if cur_node is self.head or other_node is other.head:
                return False

    # MODIFY BELOW #
    # Refer to the classes provided to understand the problems better#

    def empty(self) -> bool:
        """
        Indicates whether DLL is empty
        :return: bool True if DLL is empty, False otherwise.
        """
        return self.size==0

    def push(self, val: T, back: bool = True) -> None:
        """
        Pushes an SLLNode to the front or back of list, depending on param back
        :param value: value to push to the list
        :param back: Indicates whether to push node to front (False) or back (True)
        :return: None
        """
        if self.size == 0:
            node = Node(val)
            self.head = self.tail = node
        elif back:
            node = Node(val,None,self.tail)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(val, self.head, None)
            self.head.prev = node
            self.head = node
        self.size += 1

    def pop(self, back: bool = True) -> None:
        """
        Removes a node from the front or back of list, depending on param back
        :param back: Indicates whether to remove node from front (False) or back(True)
        :return: None
        """
        if self.size == 0:
            return
        elif self.size == 1:
            self.head = self.tail = None
        elif back:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size-=1

    def list_to_dll(self, source: List[T]) -> None:
        """
        Converts a List to a DLL after emptying self
        :param source:  source list to convert to DLL
        :return: None
        """
        self.head = self.tail = None
        self.size = 0
        if len(source) !=0:
            for elem in source:
                self.push(elem)

    def dll_to_list(self) -> List[T]:
        """
        Converts DLL to a List
        :return: List representation of self DLL
        """
        list = []
        curr = self.head
        while curr:
            list.append(curr.value)
            curr = curr.next
        return list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Constructs list of Node with value val in the DLL
        :param val: value to find in DLL
        :param find_first: If True, find first node containing val.
                           Else, find all nodes with val
        :return: List of Nodes containing value of val. Empty list if not found
        """
        list = []
        if self.size == 0:
            return list
        curr = self.head
        while curr:
            if curr.value == val:
                list.append(curr)
                if find_first:
                    break
            curr = curr.next
        return list

    def find(self, val: T) -> Node:
        """
        Finds and returns the first Node in DLL with given value
        :param val: value to look for in DLL
        :return: First node in DLL that contains val. None if not found
        """
        result = self._find_nodes(val, True)
        if len(result) == 0:
            return None
        else:
            return result[0]

    def find_all(self, val: T) -> List[Node]:
        """
        Finds and returns a list of all Node in DLL with given value
        :param val:value ot look for in DLL
        :return: List of Nodes that contain val. Empty if not found
        """
        return self._find_nodes(val)

    def _remove_node(self, to_remove: Node) -> None:
        """
        Given a reference to a Node in DLL, removes it
        :param to_remove: Node to remove from DLL
        :return: None
        """

        if self.head == to_remove:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            if self.size == 2:
                self.tail = self.head

        if to_remove.next is not None:
            to_remove.next.prev = to_remove.prev
        else:
            self.tail = to_remove.prev
            if self.tail is not None:
                self.tail.next = None
        if to_remove.prev is not None:
            to_remove.prev.next = to_remove.next
        self.size -=1

    def remove(self, val: T) -> bool:
        """
        Removes first node in DLL containing specified value
        :param val: value to remove from DLL
        :return: True if a Node is successfuly removed. Else: False
        """
        result = self.find(val)
        if result is None:
            return False
        else:
            self._remove_node(result)
            return True

    def remove_all(self, val: T) -> int:
        """
        Removes all nodes in DLL containing specified value
        :param val: value to remove from DLL
        :return: number of Nodes removed from DLL
        """
        result = self.find_all(val)
        if result is None:
            return 0
        else:
            for node in result:
                self._remove_node(node)
        return len(result)

    def reverse(self) -> None:
        """
        Reverses the order of DLL in place
        :return: None
        """
        if self.size <2:
            return
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = curr.prev
            curr.prev = next
            curr = next
        curr = self.head
        self.head = self.tail
        self.tail = curr


def fix_playlist(lst: DLL) -> bool:
    """
    Implements Floyd's Cycle Finding Algorithms to determine if 
    lst has a proper, broken, or improper loop. Will fix broken loop
    :param lst: DLL to fix
    :return: True if loop is proper or broken, will fix broken DLL,
             False if loop is improper.
    """
    state = True
    if lst.size == 0:
        return state
    if lst.size == 1:
        lst.head.next = lst.head
        lst.head.prev = lst.head
        lst.tail.next = lst.head
        lst.tail.prev = lst.head
        return state
    if lst.size == 2:
        if lst.head.next is None or lst.head.prev is None or lst.tail.prev is None or lst.tail.next is None:
            state = False
        elif lst.head.next!=lst.tail or lst.head.prev!=lst.tail or lst.tail.next!=lst.head or lst.tail.prev!=lst.head:
            state = False
        lst.head.next = lst.tail
        lst.head.prev = lst.tail
        lst.tail.next = lst.head
        lst.tail.prev = lst.head
        return state

    def fix_playlist_helper(slow: Node, fast: Node) -> bool:
        while slow and fast:
            if fast.next is None:
                return False
            if slow == fast:
                slow = slow.next
                break
            slow = slow.next
            fast = fast.next.next
        hit_head = False
        while slow:
            if slow == lst.head:
                hit_head=True
            if slow == fast:
                return hit_head
            slow = slow.next
    if lst.head.prev is None and lst.tail.next is None:
        lst.head.prev = lst.tail
        lst.tail.next = lst.head
        return state

    state = fix_playlist_helper(lst.head, lst.head.next)
    lst.head.prev = lst.tail
    lst.tail.next = lst.head
    return state
