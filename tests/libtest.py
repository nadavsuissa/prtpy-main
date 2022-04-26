import unittest
import multiwaypartition


class TestPartition(unittest.TestCase):

    def test_regular(self):
        # Regular Tests
        self.assertEqual(multiwaypartition.kwaypartition([2,3,4,5,1,2,4], 3),[[2, 1, 4], [2, 5], [3, 4]])
        self.assertEqual(multiwaypartition.kwaypartition([4,3,6,8,2,4,9], 3), [[3, 9], [4, 8], [4, 6, 2]])
        self.assertEqual(multiwaypartition.kwaypartition([5,3,6,8], 2), [[6, 5], [8, 3]])
        self.assertEqual(multiwaypartition.kwaypartition([5,3,6,7], 1),  [5,3,6,7])
        self.assertEqual(multiwaypartition.kwaypartition([4,4,4,4,4,4,4,4,4], 3), [[4, 4, 4], [4, 4, 4], [4, 4, 4]])
        self.assertEqual(multiwaypartition.kwaypartition([4,2,3,7,4,5,9,2,4,9,1,2,9,7,4,7,8,3,2,3,4,5,7,1,3,1,1,1,1,1], 10), [[1, 2, 9], [1, 2, 9], [3, 4, 5], [3, 9], [2, 7, 3], [1, 3, 8], [1, 2, 5, 4], [1, 7, 4], [1, 7, 4], [1, 7, 4]])

    def test_bad(self):
        # Regular Tests
        self.assertEqual(multiwaypartition.kwaypartition([2, 3, 4, 5, 1, 2, -4], 3), "Error: Negitive Number")
        self.assertEqual(multiwaypartition.kwaypartition([-9], 1), "Error: Negitive Number")
    def test_zero(self):
        # Regular Tests
        self.assertEqual(multiwaypartition.kwaypartition([2, 3, 4, 5, 1, 2, -4], 0), "Error: K Error")
        self.assertEqual(multiwaypartition.kwaypartition([-9], 0), "Error: K Error")

    def test_no_fair_partition(self):
            # Regular Tests
            self.assertEqual(multiwaypartition.kwaypartition([2, 3, 4, 5, 1, 2, 4,6,7,2,3,1], 5), "Error: No Fair Partition")
            self.assertEqual(multiwaypartition.kwaypartition([2, 3, 4, 5, 1, 2, 3,5,1,2,6], 4), "Error: No Fair Partition")


