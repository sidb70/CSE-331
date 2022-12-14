"""
Project 4 - Hybrid Sorting - Tests
CSE 331 Fall 2022
Bank, Nate and Abhinay
"""

import unittest
from random import seed, shuffle
from functools import cmp_to_key
from itertools import permutations

from solution import selection_sort, bubble_sort, insertion_sort, hybrid_merge_sort, sort_sushi

seed(331)


class Project4Tests(unittest.TestCase):

    def test_selection_sort(self):
        # 1. test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        selection_sort(data)
        self.assertEqual(expected, data)

        # 2. test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        selection_sort(data)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        selection_sort(data)
        self.assertEqual(expected, data)

        # 4. test empty
        data = []
        selection_sort(data)
        self.assertEqual([], data)

        # 5. test one element
        data = [331]
        selection_sort(data)
        self.assertEqual([331], data)

        # 6. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(selection_sort(data))

    def test_selection_comparator(self):

        # 1. sort negative value of itself
        data = [2, 3, 4, 2, 1, 0, 9]
        expected = sorted(data, key=lambda x: -x)
        selection_sort(data,  key=lambda x: -x)
        self.assertEqual(expected, data)

        # 2. sort strings by length
        data = ['Adam', 'Abhinay', 'Krish', 'Matt']
        expected = sorted(data, key=lambda x: len(x))
        selection_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 3. sort strings by second element
        data = ['Aaron', 'Lukas', 'Adam', 'Abhinay', 'Joshua', 'Krish', 'Matt']
        expected = sorted(data, key=lambda x: x[-1])
        selection_sort(data, key=lambda x: x[-1])
        self.assertEqual(expected, data)

        # 4. sort powers of ten by number of digits, in reverse
        data = [1, 1000000000, 1000000, 10000000000, 100000000000000,
                1000000000000, 10000, 100000000, 10000000, 10,
                1000, 100, 100000, 100000000000, 10000000000000]
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        selection_sort(data, key=lambda x: -1 * len(str(x)))
        self.assertEqual(expected, data)

        # 5. sort strings by length
        data = ['aaa', 'aaaaaaaaaaaaaa', 'a', 'aa', 'aaaaaaaa',
                'aaaaa', 'aaaaaaa', 'aaaa', 'aaaaaaaaaa', '',
                'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaaa',
                'aaaaaaaaaaaa']
        expected = sorted(data, key=lambda x: len(x))
        selection_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 6. sort strings by negative value of length
        data = ['aaa', 'aaaaaaaaaaaaaa', 'a', 'aa', 'aaaaaaaa',
                'aaaaa', 'aaaaaaa', 'aaaa', 'aaaaaaaaaa', '',
                'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaaa',
                'aaaaaaaaaaaa']
        expected = sorted(data, key=lambda x: -len(x))
        selection_sort(data, key=lambda x: -len(x))
        self.assertEqual(expected, data)

        # 7. test empty
        data = []
        selection_sort(data, key=lambda x: -x)
        self.assertEqual([], data)

        # 8. test one element
        data = [331]
        selection_sort(data, key=lambda x: -x)
        self.assertEqual([331], data)

        # 9. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(selection_sort(data, key=lambda x: -x))

    def test_selection_descending(self):
        # 1. test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data, reverse=True)
        selection_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 2. test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data, reverse=True)
        selection_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data, reverse=True)
        selection_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 4. test empty
        data = []
        selection_sort(data, descending=True)
        self.assertEqual([], data)

        # 5. test one element
        data = [331]
        selection_sort(data, descending=True)
        self.assertEqual([331], data)

        # 6. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(selection_sort(data, descending=True))

    def test_bubble_sort(self):
        # 1. test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        bubble_sort(data)
        self.assertEqual(expected, data)

        # 2. test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        bubble_sort(data)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        bubble_sort(data)
        self.assertEqual(expected, data)

        # 4. test empty
        data = []
        bubble_sort(data)
        self.assertEqual([], data)

        # 5. test one element
        data = [331]
        bubble_sort(data)
        self.assertEqual([331], data)

        # 6. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(bubble_sort(data))

    def test_bubble_comparator(self):
        # 1. sort negative value of itself
        data = [2, 3, 4, 2, 1, 0, 9]
        expected = sorted(data, key=lambda x: -x)
        bubble_sort(data, key=lambda x: -x)
        self.assertEqual(expected, data)

        # 2. sort strings by length
        data = ['Adam', 'Abhinay', 'Krish', 'Matt', 'Bank', 'Nate']
        expected = sorted(data, key=lambda x: len(x))
        bubble_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 3. sort strings by second element
        data = ['Aaron', 'Lukas', 'Adam', 'Abhinay', 'Joshua', 'Krish', 'Matt']
        expected = sorted(data, key=lambda x: x[-1])
        bubble_sort(data, key=lambda x: x[-1])
        self.assertEqual(expected, data)

        # 4. sort powers of ten by number of digits, in reverse
        data = [1, 1000000000, 1000000, 10000000000, 100000000000000,
                1000000000000, 10000, 100000000, 10000000, 10, 1000,
                100, 100000, 100000000000, 10000000000000]
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        bubble_sort(data, key=lambda x: -1 * len(str(x)))
        self.assertEqual(expected, data)

        # 5. sort strings by length
        data = ['aaa', 'aaaaaaaaaaaaaa', 'a', 'aa', 'aaaaaaaa', 'aaaaa', 'aaaaaaa',
                'aaaa', 'aaaaaaaaaa', '', 'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa',
                'aaaaaaaaaaaaa', 'aaaaaaaaaaaa']
        expected = sorted(data, key=lambda x: len(x))
        bubble_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 6. sort strings by negative value of length
        data = ['aaa', 'aaaaaaaaaaaaaa', 'a', 'aa', 'aaaaaaaa',
                'aaaaa', 'aaaaaaa', 'aaaa', 'aaaaaaaaaa', '',
                'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaaa',
                'aaaaaaaaaaaa']
        expected = sorted(data, key=lambda x: -len(x))
        bubble_sort(data, key=lambda x: -len(x))
        self.assertEqual(expected, data)

        # 7. test empty
        data = []
        bubble_sort(data,  key=lambda x: -x)
        self.assertEqual([], data)

        # 8. test one element
        data = [331]
        bubble_sort(data, key=lambda x: -x)
        self.assertEqual([331], data)

        # 9. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(bubble_sort(data, key=lambda x: -x))

    def test_bubble_descending(self):
        # 1. test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data, reverse=True)
        bubble_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 2. test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data, reverse=True)
        bubble_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data, reverse=True)
        bubble_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 4. test empty
        data = []
        bubble_sort(data, descending=True)
        self.assertEqual([], data)

        # 5. test one element
        data = [331]
        bubble_sort(data, descending=True)
        self.assertEqual([331], data)

        # 6. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(bubble_sort(data, descending=True))

    def test_insertion_sort(self):
        # 1. test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # 2. test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # 4. test empty
        data = []
        insertion_sort(data)
        self.assertEqual([], data)

        # 5. test one element
        data = [331]
        insertion_sort(data)
        self.assertEqual([331], data)

        # 6. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(insertion_sort(data))

    def test_insertion_comparator(self):
        # 1. sort negative value of itself
        data = [2, 3, 4, 2, 1, 0, 9]
        expected = sorted(data, key=lambda x: -x)
        insertion_sort(data, key=lambda x: -x)
        self.assertEqual(expected, data)

        # 2. sort strings by length
        data = ['Adam', 'Abhinay', 'Krish', 'Matt', 'Bank', 'Nate']
        expected = sorted(data, key=lambda x: len(x))
        insertion_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 3. sort strings by second element
        data = ['Aaron', 'Lukas', 'Adam', 'Abhinay', 'Joshua', 'Krish', 'Matt']
        expected = sorted(data, key=lambda x: x[-1])
        insertion_sort(data, key=lambda x: x[-1])
        self.assertEqual(expected, data)

        # 4. sort powers of ten by number of digits, in reverse
        data = [1, 1000000000, 1000000, 10000000000, 100000000000000,
                1000000000000, 10000, 100000000, 10000000,
                10, 1000, 100, 100000, 100000000000, 10000000000000]
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        insertion_sort(data, key=lambda x: -1 * len(str(x)))
        self.assertEqual(expected, data)

        # 5. sort strings by length
        data = ['aaa', 'aaaaaaaaaaaaaa', 'a', 'aa', 'aaaaaaaa', 'aaaaa', 'aaaaaaa',
                'aaaa', 'aaaaaaaaaa', '', 'aaaaaa', 'aaaaaaaaa',
                'aaaaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaa']
        expected = sorted(data, key=lambda x: len(x))
        insertion_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 6. sort strings by negative value of length
        data = ['aaa', 'aaaaaaaaaaaaaa', 'a', 'aa', 'aaaaaaaa',
                'aaaaa', 'aaaaaaa', 'aaaa', 'aaaaaaaaaa', '',
                'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaaa',
                'aaaaaaaaaaaa']
        expected = sorted(data, key=lambda x: -len(x))
        insertion_sort(data, key=lambda x: -len(x))
        self.assertEqual(expected, data)

        # 7. test empty
        data = []
        insertion_sort(data, key=lambda x: -x)
        self.assertEqual([], data)

        # 8. test one element
        data = [331]
        insertion_sort(data, key=lambda x: -x)
        self.assertEqual([331], data)

        # 9. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(insertion_sort(data, key=lambda x: -x))

    def test_insertion_descending(self):
        # 1. test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data, reverse=True)
        insertion_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 2. test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data, reverse=True)
        insertion_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data, reverse=True)
        insertion_sort(data, descending=True)
        self.assertEqual(expected, data)

        # 4. test empty
        data = []
        insertion_sort(data, descending=True)
        self.assertEqual([], data)

        # 5. test one element
        data = [331]
        insertion_sort(data, descending=True)
        self.assertEqual([331], data)

        # 6. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(insertion_sort(data, descending=True))

    def test_hybrid_merge_sort(self):
        # 1. test with basic list of integers - default comparator and threshold
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)

        # 2. test with basic set of strings - default comparator and threshold
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator and threshold
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)

        # first, all the tests from basic should work with higher thresholds

        # 4. test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        hybrid_merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # 5. test with basic set of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        hybrid_merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # 6. test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        hybrid_merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # 7. now, for a longer test - a bunch of thresholds
        data = list(range(25))
        expected = sorted(data)
        for t in range(11):
            shuffle(data)
            hybrid_merge_sort(data, threshold=t)
            self.assertEqual(expected, data)

        # 8. test empty - default comparator and threshold
        data = []
        hybrid_merge_sort(data)
        self.assertEqual([], data)

        # 9. test one element
        data = [331]
        hybrid_merge_sort(data)
        self.assertEqual([331], data)

        # 10. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(hybrid_merge_sort(data, threshold=0))

    def test_hybrid_merge_comparator(self):
        # 1. sort negative value of itself
        data = [2, 3, 4, 2, 1, 0, 9]
        expected = sorted(data, key=lambda x: -x)
        hybrid_merge_sort(data, key=lambda x: -x)
        self.assertEqual(expected, data)

        # 2. sort strings by length
        data = ['Adam', 'Abhinay', 'Krish', 'Matt', 'Bank', 'Nate']
        expected = sorted(data, key=lambda x: len(x))
        hybrid_merge_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 3. sort strings by second element
        data = ['Aaron', 'Lukas', 'Adam', 'Abhinay', 'Joshua', 'Krish', 'Matt']
        expected = sorted(data, key=lambda x: x[-1])
        hybrid_merge_sort(data, key=lambda x: x[-1])
        self.assertEqual(expected, data)

        # 4. sort powers of ten by number of digits, in reverse
        data = [10000000000, 100, 10000, 100000000, 1000000000000,
                1000000000, 1, 100000, 1000000, 10000000000000,
                100000000000, 1000, 10000000, 100000000000000, 10]
        expected = sorted(data, key=lambda x: -1 * len(str(x)))
        hybrid_merge_sort(data, key=lambda x: -1 * len(str(x)))
        self.assertEqual(expected, data)

        # 5. sort strings by length
        data = ['aaaaa', 'aaaaaaaaaaa', 'aaaa', 'a', 'aa', 'aaaaaa', 'aaa',
                'aaaaaaaaa', 'aaaaaaaaaaaaa', 'aaaaaaaaaaaa',
                'aaaaaaaaaaaaaa', 'aaaaaaa', 'aaaaaaaaaa', 'aaaaaaaa', '']
        expected = sorted(data, key=lambda x: len(x))
        hybrid_merge_sort(data, key=lambda x: len(x))
        self.assertEqual(expected, data)

        # 6. sort strings by negative value of length
        data = ['aaa', 'aaaaaaaaaaaaaa', 'a', 'aa', 'aaaaaaaa',
                'aaaaa', 'aaaaaaa', 'aaaa', 'aaaaaaaaaa', '',
                'aaaaaa', 'aaaaaaaaa', 'aaaaaaaaaaa', 'aaaaaaaaaaaaa',
                'aaaaaaaaaaaa']
        expected = sorted(data, key=lambda x: -len(x))
        hybrid_merge_sort(data, key=lambda x: -len(x))
        self.assertEqual(expected, data)

        # 7. test empty
        data = []
        hybrid_merge_sort(data, key=lambda x: -x)
        self.assertEqual([], data)

        # 8. test one element
        data = [331]
        hybrid_merge_sort(data, key=lambda x: -x)
        self.assertEqual([331], data)

        # 9. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(hybrid_merge_sort(data, key=lambda x: -x))

    def test_hybrid_merge_descending(self):
        # 1. test with basic list of integers - default comparator, threshold of zero
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data, reverse=True)
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual(expected, data)

        # 2. test with basic list of strings - default comparator, threshold
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data, reverse=True)
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual(expected, data)

        # 3. test with already sorted data - default comparator, threshold
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data, reverse=True)
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual(expected, data)

        # 4. test empty
        data = []
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual([], data)

        # 5. test one element
        data = [331]
        hybrid_merge_sort(data, threshold=0, descending=True)
        self.assertEqual([331], data)

        # 6. check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(hybrid_merge_sort(data, threshold=0, descending=True))

        # 7. now let's test with multiple thresholds
        data = list(range(50))
        expected = sorted(data, reverse=True)
        for t in range(20):
            shuffle(data)
            hybrid_merge_sort(data, threshold=t, descending=True)
            self.assertEqual(expected, data)

    def test_sort_sushi(self):
        def sushi_sort_comparator(left, right):
            """
            DO NOT MODIFY--USED TO HELP TEST
            """
            return 0 if left == right else (-1 if (left == 'D' or (left == 'A' and right == 'C')) else 1)

        # 1. test empty
        sushi = []
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        # 2. test single
        sushi = ['D']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        sushi = ['A']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        sushi = ['C']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        # 3. test very basic swaps
        sushi = ['A', 'D']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        sushi = ['C', 'D']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        sushi = ['C', 'A']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        # 4. test all three element permutations; expected is always ['D', 'A', 'C']
        sushi_original = ['D', 'A', 'C']
        perm_sushi = list(permutations(sushi_original))
        for sushi in perm_sushi:
            sushi = list(sushi)
            sort_sushi(sushi)
            self.assertEqual(sushi_original, sushi)

        sushi = ['A', 'C', 'D', 'C', 'D', 'C', 'C', 'A', 'A', 'C']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        sushi = ['C', 'C', 'D', 'D', 'D', 'A', 'D', 'A', 'D', 'D', 'D', 'A', 'D',
                 'D', 'D', 'D', 'D', 'A', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'A',
                 'C', 'C', 'C', 'C']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        # 5. Using key
        key_compare = {"D": 1, "A": 2, "C": 0}  # C -> A -> D
        shuffle(sushi)
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        sushi = ['C', 'A', 'C', 'A', 'A', 'A', 'A', 'D', 'C', 'D',
                 'C', 'A', 'D', 'A', 'A', 'C', 'D', 'C', 'C', 'C',
                 'C', 'D', 'D', 'A', 'C', 'D', 'D', 'D', 'D', 'A']
        expected = sorted(sushi, key=cmp_to_key(sushi_sort_comparator))
        sort_sushi(sushi)
        self.assertEqual(expected, sushi)

        sushi_original = ['D', 'D', 'A', 'C']
        perm_sushi = list(permutations(sushi_original))
        key_compare = {"D": 2, "A": 0, "C": 1}  # A -> C -> D
        for sushi in perm_sushi:
            sushi = list(sushi)
            sort_sushi(sushi, key=lambda x: key_compare[x])
            self.assertEqual(sorted(sushi_original, key=lambda x: key_compare[x]), sushi)

        key_compare = {"D": 1, "A": 0, "C": 2}  # A -> D -> C
        for sushi in perm_sushi:
            sushi = list(sushi)
            sort_sushi(sushi, key=lambda x: key_compare[x])
            self.assertEqual(sorted(sushi_original, key=lambda x: key_compare[x]), sushi)

        key_compare = {"D": 0, "A": 2, "C": 1}  # D -> C -> A
        for sushi in perm_sushi:
            sushi = list(sushi)
            sort_sushi(sushi, key=lambda x: key_compare[x])
            self.assertEqual(sorted(sushi_original, key=lambda x: key_compare[x]), sushi)

        sushi = ['D', 'A', 'A', 'A', 'A', 'C', 'C', 'D', 'D', 'D', 'C', 'D', 'C', 'C', 'A']
        keys = ['D', 'A', 'C']
        permu_key = list(permutations(keys))
        for key_compare in permu_key:
            key_generate = {sushi: index for index, sushi in enumerate(key_compare)}
            expected = sorted(sushi, key=lambda x: key_generate[x])
            current = sushi[:]
            sort_sushi(current, key=lambda x: key_generate[x])
            self.assertEqual(expected, current)

    def test_hybrid_merge_sort_speed(self):
        # ***WORTH NO POINTS, FOR PERSONAL TESTING PURPOSES ONLY***
        # the point of this sort is to be fast, right?
        # this (probably) won't finish if you're not careful with time complexity,
        # but it isn't a guarantee
        data = list(range(300000))
        expected = data[:]
        shuffle(data)
        hybrid_merge_sort(data)
        self.assertEqual(expected, data)


if __name__ == '__main__':
    unittest.main()
