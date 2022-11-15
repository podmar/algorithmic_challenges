import unittest

from challenges.merge_sorted_array import merge


class TestMergeBasicCase(unittest.TestCase):
    def setUp(self):
        self.nums1 = [1, 2, 3, 0, 0, 0]
        self.m = 3
        self.nums2 = [2, 5, 6]
        self.n = 3

    def test_output_is_none(self):
        """Tests is the output is None
        """

        self.assertIsNone(merge(self.nums1, self.m, self.nums2, self.n))

    def test_happy_path(self):
        """ Testing first happy path case
        """
        merge(self.nums1, self.m, self.nums2, self.n)
        self.assertEqual(self.nums1, [1, 2, 2, 3, 5, 6])


class TestMergeNum2Len0(unittest.TestCase):
    def setUp(self):
        self.nums1 = [1]
        self.m = 1
        self.nums2 = []
        self.n = 0

    def test_len_num2_0(self):
        """ Testing second array len = 0
        """
        merge(self.nums1, self.m, self.nums2, self.n)
        self.assertEqual(self.nums1, [1])


class TestMergeNum1Len0(unittest.TestCase):
    def setUp(self):
        self.nums1 = [0]
        self.m = 0
        self.nums2 = [1]
        self.n = 1

    def test_len_num1_0(self):
        """ Testing first array len = 0
        """
        merge(self.nums1, self.m, self.nums2, self.n)
        self.assertEqual(self.nums1, [1])


if __name__ == "__main__":
    unittest.main()
