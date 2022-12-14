"""
Project07
CSE 331 F22 (Onsay)
Sid Bhattacharya
solution.py
"""
import math
import queue
from typing import TypeVar, Generator, List, Tuple, Optional
from collections import Counter, deque
import json

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
# represents a Node object (forward-declare to use in Node __init__)
Node = TypeVar("Node")


####################################################################################################


class Node:
    """
    Implementation of an AVL tree node.
    Do not modify.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["value", "parent", "left", "right", "height"]

    def __init__(self, value: T, parent: Node = None,
                 left: Node = None, right: Node = None) -> None:
        """
        Construct an AVL tree node.

        :param value: value held by the node object
        :param parent: ref to parent node of which this node is a child
        :param left: ref to left child node of this node
        :param right: ref to right child node of this node
        """
        self.value = value
        self.parent, self.left, self.right = parent, left, right
        self.height = 0

    def __repr__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return f"<{str(self.value)}>"

    def __str__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return repr(self)


####################################################################################################

class AVLTree:
    """
    Implementation of an AVL tree.
    Modify only below indicated line.
    """

    __slots__ = ["origin", "size"]

    def __init__(self) -> None:
        """
        Construct an empty AVL tree.
        """
        self.origin = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the BSTree as a string.

        :return: string representation of the BST tree
        """
        if self.origin is None:
            return "Empty AVL Tree"

        lines = pretty_print_binary_tree(self.origin, 0, False, '-')[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    def __str__(self) -> str:
        """
        Represent the AVL tree as a string.

        :return: string representation of the BST tree
        """
        return repr(self)

    def visualize(self, filename="avl_tree_visualization.svg"):
        """
        Generates an svg image file of the AVL tree.

        :param filename: The filename for the generated svg file. Should end with .svg.
        Defaults to output.svg
        """
        svg_string = svg(self.origin, node_radius=20)
        with open(filename, 'w') as f:
            print(svg_string, file=f)  # This is the line that creates the file in the file system.
        return svg_string

    def height(self, root: Node) -> int:
        """
        Return height of a subtree in the AVL, properly handling the case of root = None.
        Recall that the height of an empty subtree is -1.

        :param root: root node of subtree to be measured
        :return: height of subtree rooted at `root` parameter
        """
        return root.height if root is not None else -1

    def left_rotate(self, root: Node) -> Optional[Node]:
        """
        Perform a left rotation on the subtree rooted at `root`. Return new subtree root.

        :param root: root node of unbalanced subtree to be rotated.
        :return: new root node of subtree following rotation.
        """
        if root is None:
            return None

        # pull right child up and shift right-left child across tree, update parent
        new_root, rl_child = root.right, root.right.left
        root.right = rl_child
        if rl_child is not None:
            rl_child.parent = root

        # right child has been pulled up to new root -> push old root down left, update parent
        new_root.left = root
        new_root.parent = root.parent
        if root.parent is not None:
            if root is root.parent.left:
                root.parent.left = new_root
            else:
                root.parent.right = new_root
        root.parent = new_root

        # handle tree origin case
        if root is self.origin:
            self.origin = new_root

        # update heights and return new root of subtree
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + \
                          max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    def remove(self, root: Node, val: T) -> Optional[Node]:
        """
        Remove the node with `value` from the subtree rooted at `root` if it exists.
        Return the root node of the balanced subtree following removal.

        :param root: root node of subtree from which to remove.
        :param val: value to be removed from subtree.
        :return: root node of balanced subtree.
        """
        # handle empty and recursive left/right cases
        if root is None:
            return None
        elif val < root.value:
            root.left = self.remove(root.left, val)
        elif val > root.value:
            root.right = self.remove(root.right, val)
        else:
            # handle actual deletion step on this root
            if root.left is None:
                # pull up right child, set parent, decrease size, properly handle origin-reset
                if root is self.origin:
                    self.origin = root.right
                if root.right is not None:
                    root.right.parent = root.parent
                self.size -= 1
                return root.right
            elif root.right is None:
                # pull up left child, set parent, decrease size, properly handle origin-reset
                if root is self.origin:
                    self.origin = root.left
                if root.left is not None:
                    root.left.parent = root.parent
                self.size -= 1
                return root.left
            else:
                # two children: swap with predecessor and delete predecessor
                predecessor = self.max(root.left)
                root.value = predecessor.value
                root.left = self.remove(root.left, predecessor.value)

        # update height and rebalance every node that was traversed in recursive deletion
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        return self.rebalance(root)

    ########################################
    # Implement functions below this line. #
    ########################################

    def right_rotate(self, root: Node) -> Optional[Node]:
        """
        Perform a right rotation on the subtree rooted at `root`. Return new subtree root.

        :param root: root node of unbalanced subtree to be rotated.
        :return: new root node of subtree following rotation.
        """
        if root is None:
            return None

        # pull left child up and shift left-right child across tree, update parent
        new_root, lr_child = root.left, root.left.right
        root.left = lr_child
        if lr_child is not None:
            lr_child.parent = root

        # left child has been pulled up to new root -> push old root down right, update parent
        new_root.right = root
        new_root.parent = root.parent
        if root.parent is not None:
            if root is root.parent.right:
                root.parent.right = new_root
            else:
                root.parent.left = new_root
        root.parent = new_root

        # handle tree origin case
        if root is self.origin:
            self.origin = new_root

        # update heights and return new root of subtree
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + \
                          max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    def balance_factor(self, root: Node) -> int:
        """
        Computes the balance factor of the subtree rooted at a root node
        :param root: The root Node of the subtree on which to compute the balance factor.
        :return: int representing the balance factor of root.

        """
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def rebalance(self, root: Node) -> Optional[Node]:
        """
        Rebalances the subtree rooted at root (if necessary)
        :param root: The root Node of the subtree to be rebalanced.
        :return: Root of new subtree after rebalancing (could be the original root).
        """
        root_bf = self.balance_factor(root)
        new_root = root
        if root_bf>=-1 and root_bf<=1:
            return root
        if root_bf==2:
            if self.balance_factor(root.left)==-1:
                self.left_rotate(root.left)
            new_root = self.right_rotate(root)
        else:
            if self.balance_factor(root.right)==1:
                self.right_rotate(root.right)
            new_root = self.left_rotate(root)

        if root == self.origin:
            self.origin = new_root
        return new_root

    def insert(self, root: Node, val: T) -> Optional[Node]:
        """
        Inserts a node with val into the subtree rooted at root
        :param root: the root Node of the subtree in which to insert val
        :param val: The value to be inserted in the subtree rooted at root
        :return: Root of new subtree after insertion and rebalancing (could be the original root)
        """
        if self.origin is None:
            self.origin = Node(val)
            self.size += 1
            return self.origin

        insert_pos = self.search(root,val)
        if insert_pos.value == val:
            return root

        node = Node(value=val, parent=insert_pos)
        if val<insert_pos.value:
            insert_pos.left = node
        else:
            insert_pos.right = node
        self.size += 1
        node = node.parent
        while node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
            self.rebalance(node)
            node = node.parent
        return root

    def min(self, root: Node) -> Optional[Node]:
        """
        Finds and returns the Node with the smallest value in the subtree rooted at root
        :param root: The root Node of the subtree in which to search for a minimum
        :return: Node object containing the smallest value in the subtree rooted at root
        """
        if root is None:
            return None
        if root.left is None:
            return root
        return self.min(root.left)

    def max(self, root: Node) -> Optional[Node]:
        """
        Finds and returns the Node with the largest value in the subtree rooted at root
        :param root: The root Node of the subtree in which to search for a maximum
        :return: Node object containing the largest value in the subtree rooted at root
        """
        if root is None:
            return None
        if root.right is None:
            return root
        return self.max(root.right)

    def search(self, root: Node, val: T) -> Optional[Node]:
        """
        Finds and returns Node with the value val in the subtree rooted at root
        :param root: The root Node of the subtree in which to search for val
        :param val:  The value being searched in the subtree rooted at root
        :return: Node object containing val if it exists,
                    else the Node object below which val would be inserted as a child
        """
        if self.origin is None:
            return None
        if root.value == val:
            return root
        elif val < root.value and root.left is not None:
            return self.search(root.left,val)
        elif val > root.value and root.right is not None:
            return self.search(root.right, val)
        return root

    def inorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Performs an inorder traversal of the subtree rooted at root using a Python generator
        :param root: The root Node of the subtree currently being traversed
        :return: Generator object which yields Node objects in inorder (left, node, right)
        """
        if root is not None:
            yield from self.inorder(root.left)
            yield root
            yield from self.inorder(root.right)

    def __iter__(self) -> Generator[Node, None, None]:
        """
        Dunder method that allows our AVL tree to be iterable via inorder traversal
        :return: A generator that iterates over the inorder traversal of the tree
        """
        return self.inorder(self.origin)

    def preorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Performs a preorder traversal of the subtree rooted at root using a Python generator
        :param root: The root Node of the subtree currently being traversed
        :return: Generator object which yields Node objects in preorder (node, left, right)
        """
        if root is not None:
            yield root
            yield from self.preorder(root.left)
            yield from self.preorder(root.right)

    def postorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Performs a postorder traversal of the subtree rooted at root using a Python generator
        :param root: The root Node of the subtree currently being traversed
        :return: Generator object which yields Node objects in postorder (left,right,node)
        """
        if root is not None:
            yield from self.postorder(root.left)
            yield from self.postorder(root.right)
            yield root

    def levelorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Performs a level-order traversal of the subtree rooted at root using a Python generator
        :param root: The root Node of the subtree currently being traversed
        :return: Generator object which yields Node objects in level order (breadth-first)
        """
        lev_queue = queue.SimpleQueue()
        if root is not None:
            lev_queue.put(root)
            while lev_queue.empty() is False:
                curr = lev_queue.get()
                yield curr
                if curr.left:
                    lev_queue.put(curr.left)
                if curr.right:
                    lev_queue.put(curr.right)

    ####################################################################################################

# ------- Application Problem ------- #
def is_avl_tree(tree: AVLTree):
    """
    Determines whether a given tree is a valid AVL tree by AVL properties
    :param tree: Given tree to verify
    :return: boolean indicating whether given tree is a valid AVL tree or not
    """
    if tree.origin is None or (tree.origin.left is None and tree.origin.right is None):
        return True
    def height(node):
        """
        Calculates the height of a subtree rooted at node, helper for check_balances
        :param node: root Node of the subtree whose height is being calculated
        :return: integer height of subtree rooted at node
        """
        if node is None:
            return 0
        return 1+ max(height(node.left),height(node.right))

    def check_balances(node):
        """
        Determines whether a subtree rooted at node violates the AVL balance property
        :param node: root Node of subtree being validated
        :return: boolean indicating whether the tree is balanced or not
        """
        if node is None:
            return True
        left_h = height(node.left)
        right_h = height(node.right)
        if left_h-right_h<=-2 or left_h-right_h>=2:
            return False
        is_balanced = check_balances(node.left)
        if is_balanced is False:
            return False
        is_balanced = check_balances(node.right)
        return is_balanced

    def is_ordered(node):
        """
        Determines whether a subtree rooted at node violated the BST ordering property
        :param node: root Node of subtree being validated
        :return: boolean indicating whether the tree is correctly ordered or not
        """
        if node is None:
            return True
        if (node.left and get_max(node.left) > node.value) or (node.right and get_min(node.right)<node.value):
            return False
        return is_ordered(node.left) and is_ordered(node.right)
    def get_max(node):
        """
        Determines the max value in a subtree rooted at node,helper for is_ordered
        :param node: root Node of subtree we are getting the max from
        :return: maximum value contained in the subtree rooted at node
        """
        while node.right:
            node = node.right
        return node.value
    def get_min(node):
        """
        Determines the min value in a subtree rooted at node,helper for is_ordered
        :param node: root Node of subtree we are getting the min from
        :return: minimum value contained in the subtree rooted at node
        """
        while node.left:
            node = node.left
        return node.value
    return check_balances(tree.origin) and is_ordered(tree.origin)



_SVG_XML_TEMPLATE = """
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<style>
    .value {{
        font: 300 16px monospace;
        text-align: center;
        dominant-baseline: middle;
        text-anchor: middle;
    }}
    .dict {{
        font: 300 16px monospace;
        dominant-baseline: middle;
    }}
    .node {{
        fill: lightgray;
        stroke-width: 1;
    }}
</style>
<g stroke="#000000">
{body}
</g>
</svg>
"""

_NNC_DICT_BOX_TEXT_TEMPLATE = """<text class="dict" y="{y}" xml:space="preserve">
    <tspan x="{label_x}" dy="1.2em">{label}</tspan>
    <tspan x="{bracket_x}" dy="1.2em">{{</tspan>
    {values}
    <tspan x="{bracket_x}" dy="1.2em">}}</tspan>
</text>
"""


def pretty_print_binary_tree(root: Node, curr_index: int, include_index: bool = False,
                             delimiter: str = "-", ) -> \
        Tuple[List[str], int, int, int]:
    """
    Taken from: https://github.com/joowani/binarytree

    Recursively walk down the binary tree and build a pretty-print string.
    In each recursive call, a "box" of characters visually representing the
    current (sub)tree is constructed line by line. Each line is padded with
    whitespaces to ensure all lines in the box have the same length. Then the
    box, its width, and start-end positions of its root node value repr string
    (required for drawing branches) are sent up to the parent call. The parent
    call then combines its left and right sub-boxes to build a larger box etc.
    :param root: Root node of the binary tree.
    :type root: binarytree.Node | None
    :param curr_index: Level-order_ index of the current node (root node is 0).
    :type curr_index: int
    :param include_index: If set to True, include the level-order_ node indexes using
        the following format: ``{index}{delimiter}{value}`` (default: False).
    :type include_index: bool
    :param delimiter: Delimiter character between the node index and the node
        value (default: '-').
    :type delimiter:
    :return: Box of characters visually representing the current subtree, width
        of the box, and start-end positions of the repr string of the new root
        node value.
    :rtype: ([str], int, int, int)
    .. _Level-order:
        https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
    """
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if include_index:
        node_repr = "{}{}{}".format(curr_index, delimiter, root.value)
    else:
        node_repr = f'{root.value},h={root.height},' \
                        f'???{str(root.parent.value) if root.parent else "None"}'

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = pretty_print_binary_tree(
        root.left, 2 * curr_index + 1, include_index, delimiter
    )
    r_box, r_box_width, r_root_start, r_root_end = pretty_print_binary_tree(
        root.right, 2 * curr_index + 2, include_index, delimiter
    )

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(" " * (l_root + 1))
        line1.append("_" * (l_box_width - l_root))
        line2.append(" " * l_root + "/")
        line2.append(" " * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(" " * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append("_" * r_root)
        line1.append(" " * (r_box_width - r_root + 1))
        line2.append(" " * r_root + "\\")
        line2.append(" " * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = " " * gap_size
    new_box = ["".join(line1), "".join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else " " * l_box_width
        r_line = r_box[i] if i < len(r_box) else " " * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


def svg(root: Node, node_radius: int = 16) -> str:
    """
    Taken from: https://github.com/joowani/binarytree

    Generate SVG XML.
    :param root: Generate SVG for tree rooted at root
    :param node_radius: Node radius in pixels (default: 16).
    :type node_radius: int
    :return: Raw SVG XML.
    :rtype: str
    """
    tree_height = root.height
    scale = node_radius * 3
    xml = deque()

    def scale_x(x: int, y: int) -> float:
        diff = tree_height - y
        x = 2 ** (diff + 1) * x + 2 ** diff - 1
        return 1 + node_radius + scale * x / 2

    def scale_y(y: int) -> float:
        return scale * (1 + y)

    def add_edge(parent_x: int, parent_y: int, node_x: int, node_y: int) -> None:
        xml.appendleft(
            '<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'.format(
                x1=scale_x(parent_x, parent_y),
                y1=scale_y(parent_y),
                x2=scale_x(node_x, node_y),
                y2=scale_y(node_y),
            )
        )

    def add_node(node_x: int, node_y: int, node: Node) -> None:
        x, y = scale_x(node_x, node_y), scale_y(node_y)
        xml.append(f'<circle class="node" cx="{x}" cy="{y}" r="{node_radius}"/>')
        xml.append(f'<text class="value" x="{x}" y="{y + 5}">{node.value}</text>')

    current_nodes = [root.left, root.right]
    has_more_nodes = True
    y = 1

    add_node(0, 0, root)

    while has_more_nodes:

        has_more_nodes = False
        next_nodes: List[Node] = []

        for x, node in enumerate(current_nodes):
            if node is None:
                next_nodes.append(None)
                next_nodes.append(None)
            else:
                if node.left is not None or node.right is not None:
                    has_more_nodes = True

                add_edge(x // 2, y - 1, x, y)
                add_node(x, y, node)

                next_nodes.append(node.left)
                next_nodes.append(node.right)

        current_nodes = next_nodes
        y += 1

    svg_width = scale * (2 ** tree_height)
    svg_height = scale * (2 + tree_height)

    return _SVG_XML_TEMPLATE.format(
        width=svg_width,
        height=svg_height,
        body="\n".join(xml),
    )


if __name__ == "__main__":
    pass
