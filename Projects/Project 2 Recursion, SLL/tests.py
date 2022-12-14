import unittest
from solution import RecursiveSinglyLinkedList as SLL, reverse
import random


class MyTestCase(unittest.TestCase):

    def test_push(self):

        sll = SLL()  # SLL: Empty

        # 1. Insert into an empty list
        sll.push(3)  # SLL: 3
        self.assertEqual(3, sll.head.val)  # 1
        self.assertIs(None, sll.head.next)  # 1
        self.assertEqual(3, sll.tail.val)  # 1
        self.assertIs(sll.head, sll.tail)  # 1

        # 2. Insert into a one element list
        sll.push(2)  # SLL: 3 --> 2
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(2, sll.head.next.val)  # 2
        self.assertIs(None, sll.head.next.next)  # 2
        self.assertEqual(2, sll.tail.val)  # 2
        self.assertIs(sll.head.next, sll.tail)  # 2

        # 3. Push into a list with multiple SLLNodes
        sll.push(1)  # SLL: 3 --> 2 --> 1
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(2, sll.head.next.val)  # 3
        self.assertEqual(1, sll.head.next.next.val)  # 3
        self.assertIs(None, sll.head.next.next.next)  # 3
        self.assertEqual(1, sll.tail.val)  # 3
        self.assertIs(sll.head.next.next, sll.tail)  # 3

        # 4. Front test
        sll.push(4, False)  # SLL: 4 --> 3 --> 2 --> 1
        self.assertEqual(4, sll.head.val)  # 4
        self.assertEqual(3, sll.head.next.val)  # 4
        self.assertEqual(2, sll.head.next.next.val)  # 4
        self.assertEqual(1, sll.head.next.next.next.val)  # 4
        self.assertIs(None, sll.head.next.next.next.next)  # 4
        self.assertEqual(1, sll.tail.val)  # 4
        self.assertIs(sll.head.next.next.next, sll.tail)  # 4

        # 5. Type Agnostic test
        sll = SLL()  # SLL: Empty

        sll.push('CSE331')  # SLL: CSE331
        self.assertEqual('CSE331', sll.head.val)  # 5
        self.assertIs(None, sll.head.next)  # 5
        self.assertEqual('CSE331', sll.tail.val)  # 5
        self.assertIs(sll.head, sll.tail)  # 5

        # 6. Type Agnostic test 2
        sll.push('CSE498')  # SLL: CSE331 --> CSE498
        self.assertEqual('CSE331', sll.head.val)  # 6
        self.assertEqual('CSE498', sll.head.next.val)  # 6
        self.assertIs(None, sll.head.next.next)  # 6
        self.assertEqual('CSE498', sll.tail.val)  # 6
        self.assertIs(sll.head.next, sll.tail)  # 6

    def test_to_string(self):

        sll = SLL()

        # 1. Get the string of an empty list
        self.assertEqual("None", sll.to_string(sll.head))  # 1

        # 2. Get the string of an one element list
        sll.push('C')
        self.assertEqual("C", sll.to_string(sll.head))  # 2

        # 3. Get the string of a two element list
        sll.push('S')
        self.assertEqual("C --> S", sll.to_string(sll.head))  # 3

        # 4. Get the string of a multi-element list
        sll.push('E')
        self.assertEqual("C --> S --> E", sll.to_string(sll.head))  # 4

        # 5. Get the string of another multi-element list
        sll.push("3")
        self.assertEqual("C --> S --> E --> 3", sll.to_string(sll.head))  # 5

        # 6. Get the string of another multi-element list
        sll.push("3")
        self.assertEqual("C --> S --> E --> 3 --> 3", sll.to_string(sll.head))  # 6

        # 7. Get the string of another multi-element list
        sll.push("1")
        self.assertEqual("C --> S --> E --> 3 --> 3 --> 1", sll.to_string(sll.head))  # 7

    def test_length(self):

        sll = SLL()

        # 1. Get the length of an empty list
        self.assertEqual(0, sll.length(sll.head))  # 1

        # 2. Get the length of a list with only one element
        sll.push(2)
        self.assertEqual(1, sll.length(sll.head))  # 2

        # 3. Get the length of a list with two elements
        sll.push(5)
        self.assertEqual(2, sll.length(sll.head))  # 3

        # 4. Get the length of a list with multiple elements
        sll.push(0)
        self.assertEqual(3, sll.length(sll.head))  # 4

        # 5. Get the length of another list with multiple elements
        sll.push(3)
        self.assertEqual(4, sll.length(sll.head))  # 5

    def test_sum_list(self):

        sll = SLL()

        # 1. Get the sum of an empty list
        self.assertIs(None, sll.sum_list(sll.head))  # 1

        # 2. Get the sum of a list with one SLLNode
        sll.push(3)
        self.assertEqual(3, sll.sum_list(sll.head))  # 2

        # 3. Get the sum of a list with two SLLNodes
        sll.push(5)
        self.assertEqual(8, sll.sum_list(sll.head))  # 3

        # 4. Get the sum of a list with multiple SLLNodes
        sll.push(0)
        self.assertEqual(8, sll.sum_list(sll.head))  # 4

        # 5. Get the sum of another list with multiple SLLNodes
        sll.push(1)
        self.assertEqual(9, sll.sum_list(sll.head))  # 5

        # 6. Type Agnostic test
        sll = SLL()
        sll.push('Hello')
        sll.push('World!')
        sll.push('ThereShouldBeNoSpaces')
        self.assertEqual('HelloWorld!ThereShouldBeNoSpaces', sll.sum_list(sll.head))  # 6

    def test_search(self):

        sll = SLL()

        # 1. Try to search an empty List
        self.assertEqual(False, sll.search(331))  # 1

        sll.push(4)
        sll.push(2)
        sll.push(0)

        # 2. Search for a SLLNode at the start of the list
        self.assertEqual(True, sll.search(4))  # 2

        # 3. Search for a value that doesn't exist in the list
        self.assertEqual(False, sll.search(3))  # 3

        # 4. Search for a SLLNode in the middle of the list
        self.assertEqual(True, sll.search(2))  # 4

        # 5. Search for a SLLNode at the end of the list
        self.assertEqual(True, sll.search(0))  # 5

        # 6. Type Agnostic test
        sll = SLL()
        sll.push('Hello')
        sll.push('World!')
        sll.push('ThereShouldBeNoSpaces')
        self.assertEqual(True, sll.search('World!'))  # 6

    def test_count(self):

        sll = SLL()

        # 1. Try to get a count from an empty list
        self.assertEqual(0, sll.count(7))  # 1

        # 2. Get the number of 3's in the one element list
        sll.push(3)
        self.assertEqual(1, sll.count(3))  # 2

        # 3. Get the number of 5's in the two element list
        sll.push(5)
        self.assertEqual(1, sll.count(5))  # 3

        # 4. Get the number of 0's from tha multi-element list
        sll.push(0)
        sll.push(0)
        self.assertEqual(2, sll.count(0))  # 4

        # 5. Try to get the count of a number that doesn't exist in the list
        self.assertEqual(0, sll.count(42))  # 5

        # 6. Type Agnostic test
        sll = SLL()
        sll.push('Hello')
        sll.push('World!')
        sll.push('Hello')
        self.assertEqual(2, sll.count('Hello'))  # 6

    def test_remove(self):

        sll = SLL()

        # 1. Removing from an empty list
        self.assertEqual(False, sll.remove(331))  # SLL: Empty
        self.assertIs(None, sll.head)  # 1
        self.assertIs(None, sll.tail)  # 1

        sll.push(3)
        sll.push(4)
        sll.push(3)
        sll.push(1)  # SLL: 3 --> 4 --> 3 --> 1

        # 2. Try to remove an element that doesn't exist in the list
        self.assertEqual(False, sll.remove(6))  # SLL: 3 --> 4 --> 3 --> 1
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(4, sll.head.next.val)  # 2
        self.assertEqual(3, sll.head.next.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.next.val)  # 2
        self.assertIs(None, sll.head.next.next.next.next)  # 2
        self.assertEqual(1, sll.tail.val)  # 2
        self.assertIs(sll.tail, sll.head.next.next.next)  # 2

        # 3. Remove from the middle of the list
        self.assertEqual(True, sll.remove(4))  # SLL: 3 --> 3 --> 1
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(3, sll.head.next.val)  # 3
        self.assertEqual(1, sll.head.next.next.val)  # 3
        self.assertIs(None, sll.head.next.next.next)  # 3
        self.assertEqual(1, sll.tail.val)  # 3
        self.assertIs(sll.tail, sll.head.next.next)  # 3

        # 4. Remove from the end of the list
        self.assertEqual(True, sll.remove(1))  # SLL: 3 --> 3
        self.assertEqual(3, sll.head.val)  # 4
        self.assertEqual(3, sll.head.next.val)  # 4
        self.assertIs(None, sll.head.next.next)  # 4
        self.assertEqual(3, sll.tail.val)  # 4
        self.assertIs(None, sll.tail.next)  # 4
        self.assertEqual(sll.tail, sll.head.next)  # 4

        # 5. Remove from the front of the list
        self.assertEqual(True, sll.remove(3))  # SLL: 3 (ONLY remove the first occurrence)
        self.assertEqual(3, sll.head.val)  # 5
        self.assertIs(None, sll.head.next)  # 5
        self.assertEqual(3, sll.tail.val)  # 5
        self.assertIs(sll.head, sll.tail)  # 5

        # 6. Remove the last SLLNode in the list
        self.assertEqual(True, sll.remove(3))  # SLL: Empty
        self.assertIs(None, sll.head)  # 6
        self.assertIs(None, sll.tail)  # 6

    def test_remove_all(self):
        sll = SLL()

        # 1. Removing from an empty list
        self.assertEqual(False, sll.remove_all(331))  # SLL: Empty
        self.assertIs(None, sll.head)  # 1
        self.assertIs(None, sll.tail)  # 1

        sll.push(2)
        sll.push(3)
        sll.push(4)
        sll.push(3)
        sll.push(6)
        sll.push(1)
        sll.push(6)
        sll.push(5)  # SLL: 2 --> 3 --> 4 --> 3 --> 6 --> 1 --> 6 --> 5

        # 2. Remove all the 6's
        self.assertEqual(True, sll.remove_all(6))  # SLL: 2 --> 3 --> 4 --> 3 --> 1 --> 5
        self.assertEqual(2, sll.head.val)  # 2
        self.assertEqual(3, sll.head.next.val)  # 2
        self.assertEqual(4, sll.head.next.next.val)  # 2
        self.assertEqual(3, sll.head.next.next.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.next.next.val)  # 2
        self.assertEqual(5, sll.head.next.next.next.next.next.val)  # 2
        self.assertIs(None, sll.head.next.next.next.next.next.next)  # 2
        self.assertEqual(5, sll.tail.val)  # 2
        self.assertIs(sll.tail, sll.head.next.next.next.next.next)  # 2

        # 3. Remove from the front of the list
        self.assertEqual(True, sll.remove_all(2))  # SLL: 3 --> 4 --> 3 --> 1 --> 5
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(4, sll.head.next.val)  # 3
        self.assertEqual(3, sll.head.next.next.val)  # 3
        self.assertEqual(1, sll.head.next.next.next.val)  # 3
        self.assertEqual(5, sll.head.next.next.next.next.val)  # 3
        self.assertIs(None, sll.head.next.next.next.next.next)  # 3
        self.assertEqual(5, sll.tail.val)  # 3
        self.assertIs(sll.tail, sll.head.next.next.next.next)  # 3

        # 4. Remove from the end of the list
        self.assertEqual(True, sll.remove_all(5))  # SLL: 3 --> 4 --> 3 --> 1
        self.assertEqual(3, sll.head.val)  # 4
        self.assertEqual(4, sll.head.next.val)  # 4
        self.assertEqual(3, sll.head.next.next.val)  # 4
        self.assertEqual(1, sll.head.next.next.next.val)  # 4
        self.assertIs(None, sll.head.next.next.next.next)  # 4
        self.assertEqual(1, sll.tail.val)  # 4
        self.assertIs(None, sll.tail.next)  # 4
        self.assertIs(sll.tail, sll.head.next.next.next)  # 4

        # 5. Try to remove an element that doesn't exist in the list
        self.assertEqual(False, sll.remove_all(6))  # SLL: 3 --> 4 --> 3 --> 1
        self.assertEqual(3, sll.head.val)  # 5
        self.assertEqual(4, sll.head.next.val)  # 5
        self.assertEqual(3, sll.head.next.next.val)  # 5
        self.assertEqual(1, sll.head.next.next.next.val)  # 5
        self.assertIs(None, sll.head.next.next.next.next)  # 5
        self.assertEqual(1, sll.tail.val)  # 5
        self.assertIs(sll.tail, sll.head.next.next.next)  # 5

        # 6. Remove from the middle of the list
        self.assertEqual(True, sll.remove_all(4))  # SLL: 3 --> 3 --> 1
        self.assertEqual(3, sll.head.val)  # 6
        self.assertEqual(3, sll.head.next.val)  # 6
        self.assertEqual(1, sll.head.next.next.val)  # 6
        self.assertIs(None, sll.head.next.next.next)  # 6
        self.assertEqual(1, sll.tail.val)  # 6
        self.assertIs(sll.tail, sll.head.next.next)  # 6

        # 7. Remove all of the 3's from the list
        self.assertEqual(True, sll.remove_all(3))  # SLL: 1
        self.assertEqual(1, sll.head.val)  # 7
        self.assertEqual(1, sll.tail.val)  # 7
        self.assertIs(None, sll.head.next)  # 7
        self.assertIs(sll.head, sll.tail)  # 7

        # 8. Remove the last element from the list
        self.assertEqual(True, sll.remove_all(1))  # SLL: Empty
        self.assertIs(None, sll.head)  # 8
        self.assertIs(None, sll.tail)  # 8

    def test_reverse(self):

        # 1. Try to reverse an empty list
        sll = SLL()
        reverse(sll, sll.head)
        self.assertIs(None, sll.head)  # 1
        self.assertIs(None, sll.tail)  # 1

        # 2. Reverse a one element list
        sll.push('McNamara, Cade')
        reverse(sll, sll.head)
        self.assertEqual('McNamara, Cade', sll.head.val)  # 2
        self.assertIs(None, sll.head.next)  # 2
        self.assertEqual('McNamara, Cade', sll.tail.val)  # 2
        self.assertIs(sll.head, sll.tail)  # 2

        # 3. Reverse a two element list
        sll = SLL()
        sll.push('McNamara, Cade')
        sll.push('Corum, Blake')
        reverse(sll, sll.head)
        self.assertEqual('Corum, Blake', sll.head.val)  # 3
        self.assertEqual('McNamara, Cade', sll.head.next.val)  # 3
        self.assertIs(None, sll.head.next.next)  # 3
        self.assertEqual('McNamara, Cade', sll.tail.val)  # 3
        self.assertIs(sll.head.next, sll.tail)  # 3

        # 4. Reverse a three element list
        sll = SLL()
        sll.push('Johnson, Cornelius')
        sll.push('Wilson, Roman')
        sll.push('Bell, Ronnie')
        reverse(sll, sll.head)
        self.assertEqual('Bell, Ronnie', sll.head.val)  # 4
        self.assertEqual('Wilson, Roman', sll.head.next.val)  # 4
        self.assertEqual('Johnson, Cornelius', sll.head.next.next.val)  # 4
        self.assertIs(None, sll.head.next.next.next)  # 4
        self.assertEqual('Johnson, Cornelius', sll.tail.val)  # 4
        self.assertIs(sll.head.next.next, sll.tail)  # 4

        # 5. Reverse a multi-element list
        sll = SLL()
        sll.push('Pasta')
        sll.push('Spaghetti')
        sll.push('Pizza')
        sll.push('Burger')
        reverse(sll, sll.head)
        self.assertEqual('Burger', sll.head.val)  # 5
        self.assertEqual('Pizza', sll.head.next.val)  # 5
        self.assertEqual('Spaghetti', sll.head.next.next.val)  # 5
        self.assertEqual('Pasta', sll.head.next.next.next.val)  # 5
        self.assertIs(None, sll.head.next.next.next.next)  # 5
        self.assertEqual('Pasta', sll.tail.val)  # 5
        self.assertIs(sll.head.next.next.next, sll.tail)  # 5

        # 6. Reverse a long list
        sll = SLL()
        sll.push('McNamara, Cade')
        sll.push('Corum, Blake')
        sll.push('Johnson, Cornelius')
        sll.push('Wilson, Roman')
        sll.push('Bell, Ronnie')
        sll.push('All, Erick')
        sll.push('Jones, Trente')
        sll.push('Hayes, Ryan')
        sll.push('Zinter, Zak')
        sll.push('Keegan, Trevor')
        reverse(sll, sll.head)
        self.assertEqual('Keegan, Trevor', sll.head.val)  # 6
        self.assertEqual('Zinter, Zak', sll.head.next.val)  # 6
        self.assertEqual('Hayes, Ryan', sll.head.next.next.val)  # 6
        self.assertEqual('Jones, Trente', sll.head.next.next.next.val)  # 6
        self.assertEqual('All, Erick', sll.head.next.next.next.next.val)  # 6
        self.assertEqual('Bell, Ronnie', sll.head.next.next.next.next.next.val)  # 6
        self.assertEqual('Wilson, Roman', sll.head.next.next.next.next.next.next.val)  # 6
        self.assertEqual('Johnson, Cornelius', sll.head.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual('Corum, Blake', sll.head.next.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual('McNamara, Cade', sll.head.next.next.next.next.next.next.next.next.next.val)  # 6
        self.assertIs(None, sll.head.next.next.next.next.next.next.next.next.next.next)  # 6
        self.assertEqual('McNamara, Cade', sll.tail.val)  # 6
        self.assertIs(sll.head.next.next.next.next.next.next.next.next.next, sll.tail)  # 6


if __name__ == '__main__':
    unittest.main()
