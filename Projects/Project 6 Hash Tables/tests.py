import unittest
import random
from xml.dom import minidom
from solution import HashTable, HashNode, display_duplicates

random.seed(331)


class TestProject1(unittest.TestCase):

    def test_hash(self):
        # (1) Basic with no double hashing
        table1 = HashTable(capacity=16)

        self.assertEqual(4, table1._hash("Ian"))
        self.assertEqual(2, table1._hash("Max"))
        self.assertEqual(5, table1._hash("Yash"))
        self.assertEqual(0, table1._hash("Brandon"))

        # (2) Basic with double hashing - Inserting Mode Only
        table2 = HashTable(capacity=16)

        table2.table = [None, None, None, None, HashNode("Ian", 150, True),
                        None, None, None, HashNode("H", 100),
                        None, None, None, None, None, None, None]

        self.assertEqual(9, table2._hash("Andrew", inserting=True))
        self.assertEqual(5, table2._hash("Andy", inserting=True))
        self.assertEqual(15, table2._hash("Lukas", inserting=True))

        # (3) Larger with Inserting and not Inserting
        table3 = HashTable(capacity=16)

        table3.table = [None, None, None,
                        HashNode('class_ever', 1), HashNode(None, None, True),
                        HashNode(None, None, True), None, None, None,
                        None, HashNode(None, None, True), None,
                        None, None, HashNode('cse331', 100), None]

        # Should insert in the first available bin
        self.assertEqual(4, table3._hash("is_the", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(15, table3._hash("is_the"))

        # Should insert in the first available bin
        self.assertEqual(5, table3._hash("yash", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(7, table3._hash("yash"))

        self.assertEqual(3, table3._hash("class_ever"))

        # (4) Large Comprehensive
        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        table4 = HashTable(capacity=16)

        table4.table = [None, None, HashNode('Max', 0),
                        None, HashNode('Ian', 10),
                        HashNode(None, None, True), None, None, None,
                        None, HashNode(None, None, True), None,
                        None, None, HashNode(None, None, True), None]

        expected = [2, 2, 4, 4, 9, 9, 8, 8, 8, 8, 0, 0, 8, 8, 7, 7, 6, 6, 15, 15, 3, 3, 15, 15, 14, 7, 9, 9, 1, 1, 9,
                    9, 0, 0, 5, 8, 15, 15]

        for i, key in enumerate(keys):
            # inserts every key in inserting mode and normal mode
            self.assertEqual(expected[2 * i], table4._hash(key, inserting=True))
            self.assertEqual(expected[2 * i + 1], table4._hash(key))

    def test_insert(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Insert Sanity Check
        table = HashTable()

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]

        table._insert('cse331', 100)
        table._insert('is_the', 3005)

        self.assertEqual(solution, table.table)

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table._insert('best', 42)
        table._insert('class_ever', 1)

        self.assertEqual(4, table.size)
        self.assertEqual(16, table.capacity)
        self.assertEqual(solution, table.table)

    def test_get(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Get Sanity Check
        table = HashTable(capacity=8)

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]
        table.table = solution  # set the table so insert does not need to work
        table.size = 2

        self.assertEqual(HashNode("is_the", 3005), table._get('is_the'))
        self.assertEqual(HashNode("cse331", 100), table._get('cse331'))
        self.assertIsNone(table._get('cse320'))

    def test_delete(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Delete Sanity Check
        table = HashTable(capacity=16)

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None, True), None, None, None,
                         None, None, HashNode(None, None, True), None, None, None, HashNode('cse331', 100), None]

        table.table = pre_solution  # set the table so insert does not need to work
        table.size = 4

        delete = ['best', 'is_the']
        for k in delete:
            table._delete(k)

        self.assertEqual(post_solution, table.table)
        self.assertEqual(2, table.size)

    def test_len(self):
        # (1) Empty
        table = HashTable()
        self.assertEqual(0, len(table))

        # (2) Size = 1
        table.size = 1
        self.assertEqual(1, len(table))

        # (3) Size = 5
        table.size = 5
        self.assertEqual(5, len(table))

    def test_grow(self):
        sol_keys = "Adventure Time Come on grab your friends " \
                   "We'll go to very distant lands With Jake the Dog and Finn a Human " \
                   "The fun will never end".split()
        sol_vals = [i * 100 for i in range(len(sol_keys))]

        # (1) Test grow
        table = HashTable()
        sizes = [i + 1 for i in range(len(sol_keys))]
        capacities = [8] * 3 + [16] * 4 + [32] * 8 + [64] * 11
        for i, key in enumerate(sol_keys):
            table[key] = sol_vals[i]
            self.assertEqual(sizes[i], table.size)  # 1a
            self.assertEqual(capacities[i], table.capacity)  # 1b

    def test_setitem(self):
        # (1) Simple (No Grow)
        table = HashTable()

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        self.assertEqual(2, table.size)
        self.assertEqual(8, table.capacity)
        self.assertEqual(solution, table.table)

        # (2) Simple (Grow, builds on 1)
        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table['best'] = 42
        table['class_ever'] = 1

        self.assertEqual(4, table.size)
        self.assertEqual(16, table.capacity)
        self.assertEqual(solution, table.table)

        # (3) Large Comprehensive
        table2 = HashTable()

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                    HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                    HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]

        for i, key in enumerate(keys):
            table2[key] = vals[i]

        self.assertEqual(19, table2.size)
        self.assertEqual(64, table2.capacity)
        self.assertEqual(solution, table2.table)

    def test_getitem(self):
        # (1) Basic
        table = HashTable(capacity=8)

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]
        table.table = solution  # set the table so insert does not need to work
        table.size = 2

        self.assertEqual(3005, table["is_the"])
        self.assertEqual(100, table["cse331"])

        # (2) Slightly Larger
        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table.table = solution  # set the table so insert does not need to work
        table.capacity = 16
        table.size = 4

        self.assertEqual(3005, table["is_the"])
        self.assertEqual(100, table["cse331"])
        self.assertEqual(42, table["best"])
        self.assertEqual(1, table["class_ever"])

        # (3) Large Comprehensive
        table2 = HashTable(capacity=64)

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                    HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                    HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]

        table2.table = solution  # set the table so insert does not need to work
        table2.size = 19

        for i, key in enumerate(keys):
            self.assertEqual(vals[i], table2[key])

        # (4) KeyError Check
        with self.assertRaises(KeyError):
            abc = table2["Enbody"]

    def test_delitem(self):
        # (1) Basic
        table = HashTable(capacity=16)

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None, True), None, None, None,
                         None, None, HashNode(None, None, True), None, None, None, HashNode('cse331', 100), None]

        table.table = pre_solution  # set the table so insert does not need to work
        table.size = 4

        delete = ['best', 'is_the']
        for k in delete:
            del table[k]

        self.assertEqual(post_solution, table.table)
        self.assertEqual(2, table.size)

        # (2) Large Comprehensive
        table2 = HashTable(capacity=64)

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        pre_solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                        HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                        HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                        HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                        HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                        None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                        HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                        HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]

        solution = [None, None, None, None, HashNode(None, None), None, None, None, HashNode(None, None),
                    HashNode(None, None), None, None, None, None, None, None, HashNode(None, None), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode(None, None),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode(None, None), HashNode(None, None),
                    HashNode(None, None), None, None, None, None, HashNode(None, None), None, HashNode(None, None)]

        table2.table = pre_solution  # set the table so insert does not need to work
        table2.size = 19

        for i, key in enumerate(keys):
            if i < 10:
                del table2[key]

        self.assertEqual(solution, table2.table)
        self.assertEqual(9, table2.size)

        # (3) KeyError Check
        with self.assertRaises(KeyError):
            del table2["Enbody"]
        self.assertEqual(9, table2.size)

    def test_contains(self):
        # (1) Not in Table
        table = HashTable()
        self.assertEqual(False, 'key' in table)

        # (2) In Table
        table.table[5] = HashNode('key', 331)

        self.assertEqual(True, 'key' in table)
        self.assertEqual(False, 'new_key' in table)

    def test_update(self):
        # (1) Not in Table Already
        table = HashTable()

        table.update([("minecraft", 10), ("ghast", 15)])
        self.assertEqual(10, table["minecraft"])
        self.assertEqual(15, table["ghast"])
        self.assertEqual(2, table.size)

        # (2) Update Values in Table
        table.update([("minecraft", 31), ("ghast", 42)])
        self.assertEqual(31, table["minecraft"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(2, table.size)

        # (3) Update Values in Table and Add New Values
        table.update([("minecraft", 50), ("enderman", 12)])
        self.assertEqual(50, table["minecraft"])
        self.assertEqual(12, table["enderman"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(3, table.size)

        # (4) Do Nothing
        table.update()
        self.assertEqual(50, table["minecraft"])
        self.assertEqual(12, table["enderman"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(3, table.size)

    def test_keys_values_items(self):
        # (1) Basic
        table = HashTable()

        initial_keys = ['one', 'two', 'three']
        initial_values = [1, 2, 31]
        initial_items = [('one', 1), ('two', 2), ('three', 31)]

        for i in range(3):
            table[initial_keys[i]] = initial_values[i]

        keys = table.keys()
        values = table.values()
        items = table.items()

        self.assertEqual(set(initial_keys), set(keys))
        self.assertEqual(set(initial_values), set(values))
        self.assertEqual(set(initial_items), set(items))

        # (2) Large
        table2 = HashTable()
        initial_keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach",
                        "Bank", "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        initial_values = [i * 10 for i in range(19)]
        initial_items = []

        for i, key in enumerate(initial_keys):
            table2[key] = initial_values[i]
            initial_items.append((key, initial_values[i]))

        keys = table2.keys()
        values = table2.values()
        items = table2.items()

        self.assertEqual(set(initial_keys), set(keys))
        self.assertEqual(set(initial_values), set(values))
        self.assertEqual(set(initial_items), set(items))

    def test_clear(self):
        # (1) Table with contents
        table = HashTable()

        table['table'] = 1
        table['will'] = 2
        table['be'] = 3
        table['cleared'] = 4

        self.assertEqual(4, table.size)

        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        # (2) Empty Table
        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        # (3) Reused Table
        table['one'] = 1

        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

    def test_setitem_and_delitem(self):
        # (1) Delete, then insert again (from basic delitem)
        table = HashTable(capacity=16)

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table.table = pre_solution
        table.size = 4

        delete = ['best', 'is_the']
        for k in delete:
            del table[k]

        table['best'] = 42
        table['is_the'] = 3005

        self.assertEqual(pre_solution, table.table)
        self.assertEqual(4, table.size)

        # (2) Populate, delete all (using clear), then repopulate,
        # then delete again (using delitem), then repopulate again, check if table is the same as original populate
        table = HashTable(capacity=64)
        for i in range(10):
            table[str(i)] = i

        pre_solution = table.table
        table.clear()

        for i in range(10):
            table[str(i)] = i

        self.assertEqual(pre_solution, table.table)
        self.assertEqual(10, table.size)

        for i in range(10):
            del table[str(i)]

        for i in range(10):
            table[str(i)] = i

        self.assertEqual(pre_solution, table.table)
        self.assertEqual(10, table.size)

    def test_display_duplicates(self):
        def generate_data(dirpath):
            """
            DO NOT MODIFY
            Helper for generating image hashes and filenames.
            Students can feel free to use this to get the data and filenames from the folders,
            although they need to install some packages.
            """
            import imagehash
            from PIL import Image
            import os

            path = os.path.relpath(dirpath)
            # cnt = 0
            data = []

            # Permissible Counter-Clockwise Rotation Angles
            # (images rotated these angles apart (counter-clockwise) count as duplicates)
            PCCRA = [0, 90, 180, 270]

            for root, dirs, filenames in os.walk(path):
                for file in filenames:
                    file = os.path.join(root, file)
                    img = Image.open(file)
                    # img.show()
                    # cnt += 1
                    data.append([])
                    for angle in PCCRA:
                        rotated = img.rotate(angle, expand=True)
                        data[-1].append(str(imagehash.phash(rotated)))
            # print(cnt)
            # print(data)
            return data, filenames

        # (1) Test empty
        data = []
        filenames = []
        expected = []
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (1)

        # (2) Test one image
        data = [['86719c4e5b8ca71b', 'a6a742963d4b8bb4', 'd3d9c9e40e06f2b1', 'f30d133c68e1ce1e']]
        filenames = ['c01.jpg']
        expected = [('c01.jpg', [])]
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (2)

        # (3) Test two images (not duplicates)
        data = [['b0c71acc47b33a3c', 'd4a6875833a46eb3', 'e56d4e6612196b96', '810dd2f26e0f3b39'],
                ['cc4e23b330b32773', '943e2de2c03f33cc', '99e67639651a5299', 'c1947948d5976766']]
        filenames = ['c02.jpg', 'd01.jpg']
        expected = [('c02.jpg', []), ('d01.jpg', [])]  # HashTable should look like {'c02.jpg' : [], 'd01.jpg' : []}
        actual = sorted(display_duplicates(data,
                                           filenames).items())  # This is how we will test your HashTable, note that order only matters within the duplicate lists
        self.assertEqual(expected, actual)  # (3)

        # (4) Test two images (duplicates)
        data = [['ebe87ca1c691a9c4', 'df16d2dbe2d28068', 'be422903931bfc6e', '8abc8271a778d5c3'],
                ['ebe87ca1c691a9c4', 'df16d2dbe2d28068', 'be422903931bfc6e', '8abc8271a778d5c3']]
        filenames = ['c03_1.jpg', 'c03_2.jpg']
        expected = [('c03_1.jpg', ['c03_2.jpg'])]  # HashTable should look like {'c03_1.jpg' : [c03_2.jpg]}
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (4)

        # (5) Test multiple duplicates
        data = [['c8c1460f5f2c3779', 'c05707f49dcb3aa4', '9d2b13a50ea666d3', '95fc525ec861670e'],
                ['c8c1460f5f2c3779', 'c05707f49dcb3aa4', '9d2b13a50ea666d3', '95fc525ec861670e'],
                ['c8c1460f5f2c3779', 'c05707f49dcb3aa4', '9d2b13a50ea666d3', '95fc525ec861670e']]
        filenames = ['d03_1.jpg', 'd03_2.jpg', 'd03_3.jpg']
        expected = [('d03_1.jpg', ['d03_2.jpg', 'd03_3.jpg'])]
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (5)

        # (6) Test two images (rotated duplicate)
        data = [['e7d7c78889189b07', 'ba1f80bb1e1e6155', 'b0fc9222dcb2dcac', 'af95d4104bb434be'],
                ['b0fc9222dcb2dcac', 'af95d4104bb434be', 'e7d7c78889189b07', 'ba1f80bb1e1e6155']]
        filenames = ['d04_0.jpg', 'd04_180.jpg']
        expected = [('d04_0.jpg', ['d04_180.jpg'])]
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (6)

        # (7) Test rotations
        data = [['9705695a7a587d58', '80c93a703f3f981f', 'c2af34e02ff229b2', 'd562634a4a95cdb5'],
                ['c2af34e02ff229b2', 'd562634a4a95cdb5', '9705695a7a587d58', '80c93a703f3f981f'],
                ['94ef11d91f0f07e0', 'd1ae43475e317e81', 'c16546734aa57a6b', '842656ed0b9b3b2b'],
                ['c16546734aa57a6b', '842656ed0b9b3b2b', '94ef11d91f0f07e0', 'd1ae43475e317e81'],
                ['94ef11d91f0f07e0', 'd1ae43475e317e81', 'c16546734aa57a6b', '842656ed0b9b3b2b'],
                ['842656ed0b9b3b2b', '94ef11d91f0f07e0', 'd1ae43475e317e81', 'c16546734aa57a6b'],
                ['d1ae43475e317e81', 'c16546734aa57a6b', '842656ed0b9b3b2b', '94ef11d91f0f07e0']]
        filenames = ['c04_0.jpg', 'c04_180.jpg', 'd02_0.jpg', 'd02_0_180.jpg',
                     'd02_0_d.jpg', 'd02_270.jpg', 'd02_90.jpg']
        expected = [('c04_0.jpg', ['c04_180.jpg']),
                    ('d02_0.jpg', ['d02_0_180.jpg', 'd02_0_d.jpg', 'd02_270.jpg', 'd02_90.jpg'])]
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (7)

        # (8) Pair of duplicates and a pair of non-duplicates
        data = [['9a1664c96dbc7349', '94c52e399d97c2e4', 'cfbc7163381236a3', 'c14e7b91c03d974e'],
                ['9a1664c96dbc7349', '94c52e399d97c2e4', 'cfbc7163381236a3', 'c14e7b91c03d974e'],
                ['c7237c592398d78c', '874d68c9355cca2f', '928929f377728b26', 'd2e23d6160f69e85'],
                ['e25695e0698d54f9', 'b52499dd0d99e0da', 'b7fcc24a3d270153', 'e08ecc765833b578']]
        filenames = ['c10_0.jpg', 'c10_1.jpg', 'c31.jpg', 'c33.jpg']
        expected = [('c10_0.jpg', ['c10_1.jpg']), ('c31.jpg', []), ('c33.jpg', [])]
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (8)

        # (9) Test comprehensive, some names shuffled to make sure not using filenames
        data = [['d4a6875833a46eb3', 'e56d4e6612196b96', '810dd2f26e0f3b39', 'b0c71acc47b33a3c'],
                ['ef70a10ec52cdc71', 'aa34e5bc96619a56', 'badaf4a4908689db', 'ff94b016c3cbc468'],
                ['86719c4e5b8ca71b', 'a6a742963d4b8bb4', 'd3d9c9e40e06f2b1', 'f30d133c68e1ce1e'],
                ['b0c71acc47b33a3c', 'd4a6875833a46eb3', 'e56d4e6612196b96', '810dd2f26e0f3b39'],
                ['ebe87ca1c691a9c4', 'df16d2dbe2d28068', 'be422903931bfc6e', '8abc8271a778d5c3'],
                ['9705695a7a587d58', '80c93a703f3f981f', 'c2af34e02ff229b2', 'd562634a4a95cdb5'],
                ['ef70a10ec52cdc71', 'aa34e5bc96619a56', 'badaf4a4908689db', 'ff94b016c3cbc468'],
                ['ce4339646499736d', '84363bd9b566c698', '9be96c86313326c7', 'd18c6e73e0cc9732'],
                ['bc70c30fd8900dfb', 'ad96c172936f30cc', 'e9ca96a5853a5c53', 'f83c94d8c6c56566'],
                ['d5043e7e39012dde', '816e3a473b4c31f9', '80aa6bd46dab7866', 'd4c46fec66a66452'],
                ['e4dd9b2698644d9a', 'e93994966b29319d', 'b177ce8ccdce1830', 'bc93c13c3e836437'],
                ['9a1664c96dbc7349', '94c52e399d97c2e4', 'cfbc7163381236a3', 'c14e7b91c03d974e'],
                ['b9849b2c0bbe3a39', 'e0ff9648b98b2c54', 'ec2ece865e146d91', 'b155c2f2ea0178fc'],
                ['c611312e2be6e6cb', '87783a9f18689e96', '93bb64847e4cb361', 'd2526b354cc3cb3c'],
                ['dc7863bc32b526c2', '951e6e22d0692bdb', '89d23616671f7368', 'c0b43b898dc37e71'],
                ['e0889705fff6c036', 'ee718dd248c22dc7', 'b522c2afaa5c959c', 'bbdbd8501968786c'],
                ['909f60b426df31cb', 'd5da3a2945a34db8', 'c535351e73756461', '80747f83520f387f'],
                ['db616c84964bdb94', '9b196074a6c78f39', '8ecb392ec3e18e38', 'cab135d8e26cda92'],
                ['dccf72382e227493', 'c11d3e4cd931ed8a', '8b6526937b8d2939', '94b76be68c9bb820'],
                ['c4c0331f3b3d0ec7', 'c13e6cc31e683fc2', '914a66b56a915b6d', '969479694bca6e68'],
                ['dac2a62dc65265b9', 'e930337a90c5ecec', '8f68f38793f83013', 'bc9a66d0c44fb946'],
                ['fc7c86877bb0c068', 'b624cd33cd0c3ce3', 'a9d6d36d2e1191c6', 'e38e989998a66f49'],
                ['9b6ce618672c33c9', 'b1906e6dd593aa70', 'cec6b33232c72663', 'c4382bc78039ffd8'],
                ['9539c9c93bb0c11f', 'b6cd4c32797e4906', 'c0939c636e5a95b5', 'e36719982cd45cae'],
                ['b9e1878c3c36cc93', 'f3b9cc729a81350e', 'ec4bd22569dc9919', 'a61399d8cf6b68a4'],
                ['c7237c592398d78c', '874d68c9355cca2f', '928929f377728b26', 'd2e23d6160f69e85'],
                ['c75e3271656c30d3', '81223e9c4d3beb66', '92f467db30c66171', 'd4886b261d9bb6cc'],
                ['e25695e0698d54f9', 'b52499dd0d99e0da', 'b7fcc24a3d270153', 'e08ecc765833b578'],
                ['b1cc936933da2467', 'e4aa9b5356b82d46', 'e466c6c3667071cd', 'b100cef907167ced'],
                ['c862f08ccb965dd9', 'bd1460d89be94cf4', '9dcaa5669e3c0873', 'e8be3172ce43095e'],
                ['897e0b4a653531f3', '80a64fb8f0b37173', 'dcd45fe0308f64d8', 'd51d1a16b51924fb'],
                ['8fd6b123e76890c9', 'abb2389d8537d846', 'da7ce589b282c563', 'be186937d09d8dc4'],
                ['92c50b9e39d967c1', 'd5b90a733cad3291', 'c56f5e246c73322a', '80135fd96907673b'],
                ['912de4324b699dda', 'a3d2746c4f9d1931', 'c487b1983ed3c974', 'f67829c61a37489b'],
                ['8f276c486b1f2953', '80c66afabe1bcd30', 'da8d29c236b53ce8', 'd5683f50ebb19892'],
                ['909f60b426df31cb', 'd5da3a2945a34db8', 'c535351e73756461', '80747f83520f387f'],
                ['ab5e9520d9f30678', 'acb2b592c99dc613', 'fef4c08a8c5953d2', 'f918e0389c3793b9'],
                ['bbe9e5929e84861a', 'fe97e064c9c09b1c', 'ee43b03c8b2ed3b0', 'ab31b44c9c6aceb4'],
                ['9b452c8f372d7134', '90bd2f74b486d929', '8eed79256287249e', 'c5977acee1288c8b'],
                ['ab5e9520d9f30678', 'acb2b592c99dc613', 'fef4c08a8c5953d2', 'f918e0389c3793b9'],
                ['c1fe3284ed32cc93', 'd3356c9a4aa52576', '9456672eb898d939', '869f39301f0f70dc'],
                ['d37461f9e1d17092', '9d017b3818bf9d43', '86de3453b47b2538', 'c9ab2f824d15d4e9'],
                ['c02637396d7a39b2', '80777ec8129765cd', '958c729339d86cb9', 'd5dd2a62433d3067'],
                ['c6831fda016d7ca6', 'd16907cd3658f193', '932b4a705dcf6d0c', '84c3526767f2e439'],
                ['9c5ce60ed0b15be4', 'ad942531d20eb3f9', 'c9f6b3a4851b0e4e', 'f83e709b87a42653'],
                ['e61959d42c2c5bcb', '914e8c9d6f63839c', 'b3b30c6e79864e61', 'c4e4d9273ac9d436'],
                ['935a28ed90436b6f', '98a8333773e6c748', 'c6707c47c1c93ec5', 'ed126e9d264c9ae2'],
                ['c292392fe5e06766', 'cc703a9f30e4d2e5', '97386d85b06a36ce', '99da6c35654c864f'],
                ['932c7d92d6764992', '99d3644662939d5d', 'c6c7283883dd7c39', 'cc3931e83739c8b3'],
                ['dcb42cc9731ed4e0', 'd3646b31b4191ce7', '8b1e796126b4a94f', '86ce3c9be1b2494d'],
                ['dcb42cc9731ed4e0', 'd3646b31b4191ce7', '8b1e796126b4a94f', '86ce3c9be1b2494d'],
                ['b434cb0f99a7b990', 'afdfc634322b24c1', 'e18a9ea5cc0dec3a', 'fa75939c6681606b'],
                ['b434cb0f99a7b990', 'afdfc634322b24c1', 'e18a9ea5cc0dec3a', 'fa75939c6681606b'],
                ['ccb0d3c3ac7a3263', 'f84a47988c3737c6', 'b91a8669f8d067c9', 'ade01a33d9dd6264'],
                ['ade01a33d9dd6264', 'ccb0d3c3ac7a3263', 'f84a47988c3737c6', 'b91a8669f8d067c9'],
                ['cc46337c6c8b9972', '863639cc962f64d9', '99ec669e3121ccda', 'd38c6c66c38d3173'],
                ['cc46337c6c8b9972', '863639cc962f64d9', '99ec669e3121ccda', 'd38c6c66c38d3173'],
                ['c05926cdf53b91e4', '9b3e2db156d624a1', '95f37363e091c44e', 'ce9c7c1b037c710b'],
                ['9b3e2db156d624a1', '95f37363e091c44e', 'ce9c7c1b037c710b', 'c05926cdf53b91e4'],
                ['f9a899959c94a6c5', 'ff6ec343e8e0024e', 'ac02cc3ec934f34f', 'aac496e9b94a53e4'],
                ['ac02cc3ec934f34f', 'aac496e9b94a53e4', 'f9a899959c94a6c5', 'ff6ec343e8e0024e'],
                ['fced8316c4e05ad8', 'ed30c46cc327329f', 'a947d6bc914a0f72', 'b89a91c6968d6735'],
                ['ed30c46cc327329f', 'a947d6bc914a0f72', 'b89a91c6968d6735', 'fced8316c4e05ad8'],
                ['96d5498b2d737318', 'd09d0f7839379691', 'c37f1c2178d926b2', '85335b926c9dc32b'],
                ['d09d0f7839379691', 'c37f1c2178d926b2', '85335b926c9dc32b', '96d5498b2d737318'],
                ['e1d894eb1d7423c6', 'f12a969b58d23365', 'b473c14148de766d', 'a48ac33b0d7866cf'],
                ['f12a969b58d23365', 'b473c14148de766d', 'a48ac33b0d7866cf', 'e1d894eb1d7423c6'],
                ['f815c25aac63c673', 'aa488d2f98b535ba', 'a5bf93e0f1c991c0', 'ffe0d885cd1f6210'],
                ['84ce19d3cec7338c', 'dda302cd69325ec9', 'd1644c799b6d6626', '881957773c9c1b63'],
                ['b679cbb4d0d1038e', 'bf93d023614ee790', 'e2d39a1e8479c665', 'ea38858b34e4f2ba'],
                ['d6d3f9e00687871c', 'f60d301e2d70de99', '8379ac495b2d92b6', 'a3a765b470da8b23'],
                ['80b9c6e697597835', 'f8c953b146c638b3', 'd513934cc2f32d8e', 'ad67061b136c6d39'],
                ['d340bd3cc4d37c1c', 'ac307b48f7c4855b', '8ecae897b17129d4', 'f99a2ee2226ed0e1'],
                ['f918e0389c3793b9', 'ab5e9520d9f30678', 'acb2b592c99dc613', 'fef4c08a8c5953d2'],
                ['932c7d92d6764992', '99d3644662939d5d', 'c6c7283883dd7c39', 'cc3931e83739c8b3'],
                ['f30d133c68e1ce1e', '86719c4e5b8ca71b', 'a6a742963d4b8bb4', 'd3d9c9e40e06f2b1'],
                ['ab5e9520d9f30678', 'acb2b592c99dc613', 'fef4c08a8c5953d2', 'f918e0389c3793b9'],
                ['ce4339646499736d', '84363bd9b566c698', '9be96c86313326c7', 'd18c6e73e0cc9732'],
                ['acb2b592c99dc613', 'fef4c08a8c5953d2', 'f918e0389c3793b9', 'ab5e9520d9f30678'],
                ['ab5e9520d9f30678', 'acb2b592c99dc613', 'fef4c08a8c5953d2', 'f918e0389c3793b9'],
                ['be422903931bfc6e', '8abc8271a778d5c3', 'ebe87ca1c691a9c4', 'df16d2dbe2d28068'],
                ['909f60b426df31cb', 'd5da3a2945a34db8', 'c535351e73756461', '80747f83520f387f'],
                ['c2af34e02ff229b2', 'd562634a4a95cdb5', '9705695a7a587d58', '80c93a703f3f981f']]
        filenames = ['a.jpg', 'alpha.jpg', 'c01.jpg', 'c02.jpg', 'c03.jpg', 'c04.jpg', 'c05.jpg', 'c06.jpg', 'c07.jpg',
                     'c08.jpg', 'c09.jpg', 'c10.jpg', 'c11.jpg', 'c12.jpg', 'c13.jpg', 'c14.jpg', 'c22.jpg', 'c23.jpg',
                     'c24.jpg', 'c25.jpg', 'c26.jpg', 'c27.jpg', 'c28.jpg', 'c29.jpg', 'c30.jpg', 'c31.jpg', 'c32.jpg',
                     'c33.jpg', 'c34.jpg', 'c35.jpg', 'c36.jpg', 'c41.jpg', 'c42.jpg', 'c43.jpg', 'c44.jpg', 'cute.jpg',
                     'cutedoggy.jpg', 'd15.jpg', 'd16.jpg', 'd17.jpg', 'd18.jpg', 'd19.jpg', 'd20.jpg', 'd21.jpg',
                     'd22.jpg', 'd23.jpg', 'd24.jpg', 'd25.jpg', 'd26.jpg', 'd27.jpg', 'd27_d.jpg', 'd28.jpg',
                     'd28_d.jpg', 'd29.jpg', 'd29_d.jpg', 'd30.jpg', 'd30_d.jpg', 'd31.jpg', 'd31_d.jpg', 'd32.jpg',
                     'd32_d.jpg', 'd33.jpg', 'd33_d.jpg', 'd34.jpg', 'd34_d.jpg', 'd35.jpg', 'd35_d.jpg', 'd36.jpg',
                     'd37.jpg', 'd38.jpg', 'd39.jpg', 'd49_d.jpg', 'd50.jpg', 'dog.jpg', 'dupe.jpg', 'r4.jpg',
                     'randomdupe.jpg', 'rand_dupe1.jpg', 'sidewaysdog.jpg', 'small.jpg', 't.jpg', 'upsidedown.jpg',
                     'x.jpg']
        expected = [('a.jpg', ['c02.jpg']), ('alpha.jpg', ['c05.jpg']), ('c01.jpg', ['r4.jpg']), ('c03.jpg', ['t.jpg']),
                    ('c04.jpg', ['x.jpg']), ('c06.jpg', ['rand_dupe1.jpg']), ('c07.jpg', []), ('c08.jpg', []),
                    ('c09.jpg', []), ('c10.jpg', []), ('c11.jpg', []), ('c12.jpg', []), ('c13.jpg', []),
                    ('c14.jpg', []), ('c22.jpg', ['cute.jpg', 'upsidedown.jpg']), ('c23.jpg', []), ('c24.jpg', []),
                    ('c25.jpg', []), ('c26.jpg', []), ('c27.jpg', []), ('c28.jpg', []), ('c29.jpg', []),
                    ('c30.jpg', []), ('c31.jpg', []), ('c32.jpg', []), ('c33.jpg', []), ('c34.jpg', []),
                    ('c35.jpg', []), ('c36.jpg', []), ('c41.jpg', []), ('c42.jpg', []), ('c43.jpg', []),
                    ('c44.jpg', []),
                    ('cutedoggy.jpg', ['d17.jpg', 'dog.jpg', 'randomdupe.jpg', 'sidewaysdog.jpg', 'small.jpg']),
                    ('d15.jpg', []), ('d16.jpg', []), ('d18.jpg', []), ('d19.jpg', []), ('d20.jpg', []),
                    ('d21.jpg', []), ('d22.jpg', []), ('d23.jpg', []), ('d24.jpg', []), ('d25.jpg', []),
                    ('d26.jpg', ['dupe.jpg']), ('d27.jpg', ['d27_d.jpg']), ('d28.jpg', ['d28_d.jpg']),
                    ('d29.jpg', ['d29_d.jpg']), ('d30.jpg', ['d30_d.jpg']), ('d31.jpg', ['d31_d.jpg']),
                    ('d32.jpg', ['d32_d.jpg']), ('d33.jpg', ['d33_d.jpg']), ('d34.jpg', ['d34_d.jpg']),
                    ('d35.jpg', ['d35_d.jpg']), ('d36.jpg', []), ('d37.jpg', []), ('d38.jpg', []), ('d39.jpg', []),
                    ('d49_d.jpg', []), ('d50.jpg', [])]
        actual = sorted(display_duplicates(data, filenames).items())
        self.assertEqual(expected, actual)  # (9)


if __name__ == '__main__':
    unittest.main()
