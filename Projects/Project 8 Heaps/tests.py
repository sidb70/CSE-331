from random import randint
from random import seed
from string import ascii_lowercase
from solution import MinHeap, MaxHeap, get_eating_times
import unittest
import sys

sys.modules["heapq"] = None  # Don't use outside heap modules!


class TestProject08(unittest.TestCase):
    def test_length_empty(self):
        # (1) Zero Element Heap
        heap = MinHeap()
        self.assertEqual(True, heap.empty())  # (1)
        self.assertEqual(0, len(heap))  # (1)

        # (2) One Element Heap
        heap.data = [4]
        self.assertEqual(False, heap.empty())  # (2)
        self.assertEqual(1, len(heap))  # (2)

        # (3) Three Element Heap
        heap.data = [1, 4, 7]
        self.assertEqual(False, heap.empty())  # (3)
        self.assertEqual(3, len(heap))  # (3)

        # (4) Many Element Heap
        heap.data = [1, 2, 3, 4, 5]
        self.assertEqual(False, heap.empty())  # (4)
        self.assertEqual(5, len(heap))  # (4)

        # (5) Many Element Heap (Out of Order)
        heap.data = [1, 3, 2, 8, 5, 6, 9]
        self.assertEqual(False, heap.empty())  # (5)
        self.assertEqual(7, len(heap))  # (5)

    def test_top_minheap(self):
        # (1) Zero Element Heap
        heap = MinHeap()
        self.assertEqual(None, heap.top())  # (1)

        # (2) One Element Heap
        heap.data = [4]
        self.assertEqual(4, heap.top())  # (2)

        # (3) Three Element Heap
        heap.data = [1, 4, 7]
        self.assertEqual(1, heap.top())  # (3)

        # (4) Many Element Heap
        heap.data = [2, 2, 3, 4, 5]
        self.assertEqual(2, heap.top())  # (4)

        # (5) Many Element Heap (Out of Order)
        heap.data = [0, 3, 4, 8, 5, 6, 9]
        self.assertEqual(0, heap.top())  # (5)

    def test_get_left_child_index(self):

        # (1) One Element Heap
        heap = MinHeap()
        heap.data = [4]
        self.assertEqual(None, heap.get_left_child_index(0))  # (1)

        # (2) Two Element Heap
        heap.data = [1, 4]
        self.assertEqual(1, heap.get_left_child_index(0))  # (2)
        self.assertEqual(None, heap.get_left_child_index(1))  # (2)

        # (3) Many Element Heap
        heap.data = [1, 2, 3, 4, 5]
        self.assertEqual(1, heap.get_left_child_index(0))  # (3)
        self.assertEqual(3, heap.get_left_child_index(1))  # (3)
        self.assertEqual(None, heap.get_left_child_index(2))  # (3)
        self.assertEqual(None, heap.get_left_child_index(3))  # (3)
        self.assertEqual(None, heap.get_left_child_index(4))  # (3)

        # (4) Out of Bounds
        heap.data = [1, 2, 3, 4, 5]
        self.assertEqual(None, heap.get_left_child_index(5))  # (4)
        self.assertEqual(None, heap.get_left_child_index(6))  # (4)
        self.assertEqual(None, heap.get_left_child_index(7))  # (4)
        self.assertEqual(None, heap.get_left_child_index(331))  # (4)

    def test_get_right_child_index(self):

        # (1) One Element Heap
        heap = MinHeap()
        heap.data = [4]
        self.assertEqual(None, heap.get_right_child_index(0))  # (1)

        # (2) Three Element Heap
        heap.data = [1, 4, 7]
        self.assertEqual(2, heap.get_right_child_index(0))  # (2)
        self.assertEqual(None, heap.get_right_child_index(1))  # (2)
        self.assertEqual(None, heap.get_right_child_index(2))  # (2)

        # (3) Many Element Heap
        heap.data = [1, 2, 3, 4, 5]
        self.assertEqual(2, heap.get_right_child_index(0))  # (3)
        self.assertEqual(4, heap.get_right_child_index(1))  # (3)
        self.assertEqual(None, heap.get_right_child_index(2))  # (3)
        self.assertEqual(None, heap.get_right_child_index(3))  # (3)
        self.assertEqual(None, heap.get_right_child_index(4))  # (3)

        # (4) Out of Bounds
        heap.data = [1, 2, 3, 4, 5]
        self.assertEqual(None, heap.get_right_child_index(5))  # (4)
        self.assertEqual(None, heap.get_right_child_index(6))  # (4)
        self.assertEqual(None, heap.get_right_child_index(7))  # (4)
        self.assertEqual(None, heap.get_right_child_index(331))  # (4)

    def test_get_parent_index(self):
        # (1) One Element Heap
        heap = MinHeap()
        heap.data = [4]
        self.assertEqual(None, heap.get_parent_index(0))  # (1)

        # (2) Three Element Heap
        heap.data = [1, 4, 7]
        self.assertEqual(None, heap.get_parent_index(0))  # (2)
        self.assertEqual(0, heap.get_parent_index(1))  # (2)
        self.assertEqual(0, heap.get_parent_index(2))  # (2)

        # (3) Many Element Heap
        heap.data = [1, 2, 3, 4, 5]
        self.assertEqual(None, heap.get_parent_index(0))  # (3)
        self.assertEqual(0, heap.get_parent_index(1))  # (3)
        self.assertEqual(0, heap.get_parent_index(2))  # (3)
        self.assertEqual(1, heap.get_parent_index(3))  # (3)
        self.assertEqual(1, heap.get_parent_index(4))  # (3)

    def test_min_child(self):
        # (1) One Element Heap
        heap = MinHeap()
        heap.data = [4]
        self.assertEqual(None, heap.get_min_child_index(0))  # (1)

        # (2) Three Element Heap
        heap.data = [1, 4, 7]
        self.assertEqual(1, heap.get_min_child_index(0))  # (2)
        self.assertEqual(None, heap.get_min_child_index(1))  # (2)
        self.assertEqual(None, heap.get_min_child_index(2))  # (2)

        # (3) Many Element Heap
        heap.data = [1, 2, 3, 4, 5]
        self.assertEqual(1, heap.get_min_child_index(0))  # (3)
        self.assertEqual(3, heap.get_min_child_index(1))  # (3)
        self.assertEqual(None, heap.get_min_child_index(2))  # (3)
        self.assertEqual(None, heap.get_min_child_index(3))  # (3)
        self.assertEqual(None, heap.get_min_child_index(4))  # (3)

        # (4) Many Element Heap (Out of Order)
        heap.data = [1, 3, 2, 8, 5, 6, 9]
        self.assertEqual(2, heap.get_min_child_index(0))  # (4)
        self.assertEqual(4, heap.get_min_child_index(1))  # (4)
        self.assertEqual(5, heap.get_min_child_index(2))  # (4)
        self.assertEqual(None, heap.get_min_child_index(3))  # (4)
        self.assertEqual(None, heap.get_min_child_index(4))  # (4)
        self.assertEqual(None, heap.get_min_child_index(5))  # (4)
        self.assertEqual(None, heap.get_min_child_index(6))  # (4)

        # (5) Many Element Heap (Node With Single Child)
        heap.data = [1, 3, 2, 8]
        self.assertEqual(2, heap.get_min_child_index(0))  # (5)
        self.assertEqual(3, heap.get_min_child_index(1))  # (5)
        self.assertEqual(None, heap.get_min_child_index(2))  # (5)
        self.assertEqual(None, heap.get_min_child_index(3))  # (5)

        # (6) Out of Bounds
        heap.data = [1, 3, 2, 8]
        self.assertEqual(None, heap.get_min_child_index(4))  # (6)
        self.assertEqual(None, heap.get_min_child_index(5))  # (6)
        self.assertEqual(None, heap.get_min_child_index(6))  # (6)
        self.assertEqual(None, heap.get_min_child_index(331))  # (6)

    def test_push_minheap(self):
        """
        push cases, requires functioning accessors and percolates
        """
        seed(5)

        # (1) Simple Case (Percolate Not Needed)
        heap = MinHeap()
        heap.push(1)
        heap.push(2)
        heap.push(3)
        heap.push(5)
        heap.push(7)
        heap.push(9)

        self.assertEqual(6, len(heap.data))  # (1) Length of heap is 6
        self.assertEqual({1, 2, 3, 5, 7, 9}, set(heap.data))  # (1) Heap has correct elements
        self.assertEqual(heap.data[0], min(heap.data[:6]))  # (1) Top of the heap is the minimum element
        self.assertLess(heap.data[1], heap.data[3])  # (1) Ensure less than children
        self.assertLess(heap.data[1], heap.data[4])  # (1) Ensure less than children
        self.assertLess(heap.data[2], heap.data[5])  # (1) Node at index 2 is less than Node at index 5

        # (2) Simple Case (Percolate)
        heap = MinHeap()
        heap.push(5)
        heap.push(4)
        heap.push(3)
        self.assertEqual(3, len(heap.data))  # (2) Length of heap is 3
        self.assertEqual({3, 4, 5}, set(heap.data))  # (2) Heap has correct elements
        self.assertEqual(heap.data[0], min(heap.data[:3]))  # (2) Top of the heap is the minimum element
        self.assertEqual(3, heap.data[0])  # (2) Top of the heap is the minimum element

        # (3) Adding to Test case (2) (More Percolating)
        heap.push(2)
        heap.push(6)
        heap.push(7)

        self.assertEqual(6, len(heap.data))  # (3) Length of heap is 6
        self.assertEqual({2, 3, 4, 5, 6, 7}, set(heap.data))  # (3) Heap has correct elements
        self.assertEqual(heap.data[0], min(heap.data[:6]))  # (3) Top of the heap is the minimum element
        self.assertLess(heap.data[1], heap.data[3])  # (3) Ensure less than children
        self.assertLess(heap.data[1], heap.data[4])  # (3) Ensure less than children
        self.assertLess(heap.data[2], heap.data[5])  # (3) Node at index 2 is less than Node at index 5

        # (4) Larger input
        heap = MinHeap()
        pushed = set()
        for i in range(20):
            num = randint(1, 100)
            heap.push(num)  # adding random numbers
            pushed.add(num)

        # Assert heap data has proper length
        self.assertEqual(20, len(heap.data))
        # Assert that the heap's data contains the correct elements
        self.assertEqual(pushed, set(heap.data))

        for i in range(len(heap.data)):
            # Assert that for each Node in the heap, the children of the node are greater than itself
            if heap.get_left_child_index(i):
                self.assertLessEqual(heap.data[i], heap.data[heap.get_left_child_index(i)])  # (4)
            if heap.get_right_child_index(i):
                self.assertLessEqual(heap.data[i], heap.data[heap.get_right_child_index(i)])  # (4)

    def test_pop_minheap(self):
        """
        pop cases, requires functioning accessors and percolates
        """
        # (1) Pop root off one element heap
        heap = MinHeap()
        heap.pop()  # Test popping from empty heap doesn't crash

        heap.data = [5]
        self.assertEqual(5, heap.pop())  # (1)
        self.assertEqual(0, len(heap))  # (1)
        self.assertEqual([], heap.data)  # (1)

        # (2) Three Element Heap (no percolating)
        heap = MinHeap()
        heap.data = [3, 5, 4]
        self.assertEqual(3, heap.pop())  # (2)
        self.assertEqual(2, len(heap))  # (2)
        self.assertEqual([4, 5], heap.data)  # (2)

        # (3) Three Element Heap (percolating)
        heap = MinHeap()
        heap.data = [3, 4, 5]
        self.assertEqual(3, heap.pop())  # (3)
        self.assertEqual(2, len(heap))  # (3)
        self.assertEqual([4, 5], heap.data)  # (3)

        # (4) Many Element Heap (percolating)
        heap = MinHeap()
        heap.data = [1, 3, 2, 6, 7, 4, 14]
        self.assertEqual(1, heap.pop())  # (4)
        self.assertEqual(6, len(heap))  # (4)
        self.assertEqual([2, 3, 4, 6, 7, 14], heap.data)  # (4)

        self.assertEqual(2, heap.pop())  # (4)
        self.assertEqual(5, len(heap))  # (4)
        self.assertEqual([3, 6, 4, 14, 7], heap.data)  # (4)

        self.assertEqual(3, heap.pop())  # (4)
        self.assertEqual(4, len(heap))  # (4)
        self.assertEqual([4, 6, 7, 14], heap.data)  # (4)

        # (5) Large dataset
        heap = MinHeap()
        correct = [i for i in range(1, 20)]
        student = list()
        for i in range(20, 0, -1):
            heap.push(i)
        for _ in range(19):
            student.append(heap.pop())
        self.assertEqual(correct, student)  # (5) Minimum element is always popped first

    def test_top_maxheap(self):
        # (1) Zero Element Heap
        heap = MaxHeap()
        self.assertEqual(None, heap.top())  # (1)

        # (2) One Element Heap
        heap.data.data = [-4]
        self.assertEqual(4, heap.top())  # (2)

        # (3) Three Element Heap
        heap.data.data = [-7, -4, -1]
        self.assertEqual(7, heap.top())  # (3)

        # (4) Many Element Heap (and negative values!)
        heap.data.data = [2, 2, 3, 4, 5]
        self.assertEqual(-2, heap.top())  # (4)

        # (5) Many Element Heap (Out of Order)
        heap.data.data = [-9, -7, -8, -2, -3, -1, 3]
        self.assertEqual(9, heap.top())  # (5)

    def test_push_maxheap(self):
        """
        push cases, requires functioning accessors and percolates
        """
        seed(5)

        # (1) Simple Case (Percolate Not Needed)
        heap = MaxHeap()
        heap.push(9)
        heap.push(7)
        heap.push(5)
        heap.push(3)
        heap.push(2)
        heap.push(1)
        self.assertEqual(6, len(heap.data))  # (1) Length of heap is 6
        self.assertEqual({-1, -2, -3, -5, -7, -9}, set(heap.data.data))  # (1) Heap has correct elements
        self.assertEqual(heap.data.data[0], min(heap.data.data[:6]))  # (1) Top of the heap is the maximum element
        self.assertLess(heap.data.data[1], heap.data.data[3])  # (1) Ensure less than children
        self.assertLess(heap.data.data[1], heap.data.data[4])  # (1) Ensure less than children
        self.assertLess(heap.data.data[2], heap.data.data[5])  # (1) Node at index 2 is less than Node at index 5

        # (2) Simple Case (Percolate)
        heap = MaxHeap()
        heap.push(3)
        heap.push(4)
        heap.push(5)
        self.assertEqual(3, len(heap.data.data))  # (2) Length of heap is 3
        self.assertEqual({-3, -4, -5}, set(heap.data.data))  # (2) Heap has correct elements
        self.assertEqual(heap.data.data[0], min(heap.data.data[:3]))  # (2) Top of the heap is the maximum element
        self.assertEqual(5, heap.top())  # (2) Top of the heap is the maximum element

        # (3) Adding to Test case (2) (More Percolating)
        heap.push(2)
        heap.push(6)
        heap.push(7)

        self.assertEqual(6, len(heap.data))  # (3) Length of heap is 6
        self.assertEqual({-2, -3, -4, -5, -6, -7}, set(heap.data.data))  # (3) Heap has correct elements
        self.assertEqual(heap.data.data[0], min(heap.data.data[:6]))  # (3) Top of the heap is the maximum element
        self.assertLess(heap.data.data[1], heap.data.data[3])  # (3) Ensure greater than children
        self.assertLess(heap.data.data[1], heap.data.data[4])  # (3) Ensure greater than children
        self.assertLess(heap.data.data[2], heap.data.data[5])  # (3) Node at index 2 is greater than Node at index 5

        # (4) Larger input
        heap = MaxHeap()
        pushed = set()
        for i in range(20):
            num = randint(1, 100)
            heap.push(num)  # adding random numbers
            pushed.add(-num)

        # Assert heap data has proper length
        self.assertEqual(20, len(heap.data))  # (4)
        # Assert that the heap's data contains the correct elements
        self.assertEqual(pushed, set(heap.data.data))  # (4)

        for i in range(len(heap.data)):
            # Assert that for each Node in the heap, the children of the node are greater than itself
            if heap.data.get_left_child_index(i):
                self.assertLessEqual(heap.data.data[i], heap.data.data[heap.data.get_left_child_index(i)])  # (4)
            if heap.data.get_right_child_index(i):
                self.assertLessEqual(heap.data.data[i], heap.data.data[heap.data.get_right_child_index(i)])  # (4)

    def test_pop_maxheap(self):
        """
        pop cases, requires accessors
        """
        # (1) Pop root off one element heap
        heap = MaxHeap()
        heap.data.data = [-5]
        self.assertEqual(5, heap.pop())  # (1)
        self.assertEqual(0, len(heap))  # (1)
        self.assertEqual([], heap.data.data)  # (1)

        # (2) Three Element Heap (no percolating)
        heap = MaxHeap()
        heap.data.data = [-5, -3, -4]
        self.assertEqual(5, heap.pop())  # (2)
        self.assertEqual(2, len(heap))  # (2)
        self.assertEqual(4, heap.top())  # (2)

        # (3) Three Element Heap (percolating)
        heap = MaxHeap()
        heap.data.data = [-5, -4, -3]
        self.assertEqual(5, heap.pop())  # (3)
        self.assertEqual(2, len(heap))  # (3)
        self.assertEqual(4, heap.top())  # (3)

        # (4) Many Element Heap (percolating)
        heap = MaxHeap()
        heap.data.data = [-14, -6, -13, -4, -5, -8, -1]
        self.assertEqual(14, heap.pop())  # (4)
        self.assertEqual(6, len(heap))  # (4)
        self.assertEqual(13, heap.top())  # (4)

        self.assertEqual(13, heap.pop())  # (4)
        self.assertEqual(5, len(heap))  # (4)
        self.assertEqual(8, heap.top())  # (4)

        self.assertEqual(8, heap.pop())  # (4)
        self.assertEqual(4, len(heap))  # (4)
        self.assertEqual(6, heap.top())  # (4)

        # (5) Large dataset
        heap = MaxHeap()
        correct = [i for i in range(19, 0, -1)]
        student = list()
        for i in range(1, 20):
            heap.push(i)
        for _ in range(19):
            student.append(heap.pop())
        self.assertEqual(correct, student)  # (5) Maximum element is always popped first

    def test_nonint(self):
        # Test minheap with non integer type
        student_min_heap = MinHeap()
        test_list = ['e', 'c', 'b', 'd', 'a', 'f']
        for node in test_list:
            student_min_heap.push(node)

        expected = ['a', 'b', 'c', 'd', 'e', 'f']
        actual = []
        for _ in range(len(student_min_heap)):
            actual.append(student_min_heap.pop())
        self.assertEqual(expected, actual)

    def test_application(self):
        # Empty input
        test_empty = []
        expected = []
        actual = get_eating_times(test_empty)
        self.assertEqual(expected, actual)  # Empty input test

        # Make sure zero length intervals are not included in the output
        # If you're failing this, you're probably using < instead of <=
        test_zero_length_not_included = [[[1, 2], [2, 3]]]
        expected = []
        actual = get_eating_times(test_zero_length_not_included)
        self.assertEqual(expected, actual)  # Zero length intervals not included test

        # All intervals overlap with each other, result should be an empty output
        test_all_overlapping = [[[1, 3], [1, 2], [1, 4]], [[3, 10], [5, 7]], [[6, 8]], [[9, 15], [11, 18]], [[12, 17],
                                                                                                             [15, 22]]]
        expected = []
        actual = get_eating_times(test_all_overlapping)
        self.assertEqual(expected, actual)  # All intervals overlapping test

        # A test with a really wide interval so that brute force solutions don't work
        test_long_interval = [[[6, 100000000]], [[100000003, 100000005]]]
        expected = [[100000000, 100000003]]
        actual = get_eating_times(test_long_interval)
        self.assertEqual(expected, actual)  # Long interval test

        # 1
        test1 = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
        expected = [[3, 4]]
        actual = get_eating_times(test1)
        self.assertEqual(expected, actual)  # 1

        # 2
        test2 = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
        expected = [[5, 6], [7, 9]]
        actual = get_eating_times(test2)
        self.assertEqual(expected, actual)  # 2

        # 3
        test3 = [[[1, 3]], [[16, 21], [69, 71], [90, 99]], [[18, 23], [65, 69]], [[4, 10], [23, 28],
                                                                                  [42, 48], [68, 77], [88, 89]],
                 [[14, 24], [30, 34], [35, 42], [68, 73], [93, 96]]]
        expected = [[3, 4], [10, 14], [28, 30], [34, 35], [48, 65], [77, 88], [89, 90]]
        actual = get_eating_times(test3)
        self.assertEqual(expected, actual)  # 3

        # 4
        test4 = [[[4, 8], [15, 25], [42, 51], [65, 73], [98, 100]], [[8, 10], [92, 101]],
                 [[3, 5], [88, 92]], [[41, 44]], [[10, 14], [28, 37], [96, 106]]]
        expected = [[14, 15], [25, 28], [37, 41], [51, 65], [73, 88]]
        actual = get_eating_times(test4)
        self.assertEqual(expected, actual)  # 4

        # 5
        test5 = [[[14, 16], [27, 32], [51, 57], [68, 76]], [[4, 8]], [[8, 17], [35, 43], [48, 49], [59, 66], [81, 85]]]
        expected = [[17, 27], [32, 35], [43, 48], [49, 51], [57, 59], [66, 68], [76, 81]]
        actual = get_eating_times(test5)
        self.assertEqual(expected, actual)  # 5


if __name__ == "__main__":
    unittest.main()
