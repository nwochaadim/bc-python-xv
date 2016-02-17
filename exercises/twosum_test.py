import unittest
from twosum import twosum

class TwoSumTestSuite(unittest.TestCase):

	def test_list_range_4(self):
		res = twosum([2, 5, 1, 7], 8)
		self.assertEqual(res, [2, 3])

	def test_list_range_5(self):
		res = twosum([2, 5, 1, 7, 9], 10)
		self.assertEqual(res, [2, 4])

	def test_list_range_6(self):
		res = twosum([2, 5, 1, 7, 9, 6], 12)
		self.assertEqual(res, [1, 3])

	def test_list_range_7(self):
		res = twosum([2, 5, 1, 7, 9, 6, 4], 10)
		self.assertEqual(res, [2, 4])

	def test_list_range_8(self):
		res = twosum([2, 5, 1, 7, 9, 6, 10, 14], 13)
		self.assertEqual(res, [3, 5])

	def test_list_range_9(self):
		res = twosum([2, 5, 1, 7, 9, 6, 4, 20, 4, 9], 14)
		self.assertEqual(res, [1, 4])

	def test_list_range_10(self):
		res = twosum([2, 5, 1, 7, 9, 6, 4, 8, 4, 13], 16)
		self.assertEqual(res, [3, 4])

	def test_list_range_11(self):
		res = twosum([10, 5, 1, 7, 9, 6, 4, 8, 4, 9, 13, 18], 20)
		self.assertEqual(res, [3, 10])

	def test_list_range_12(self):
		res = twosum([2, 14, 1, 7, 9, 6, 19, 8, 16, 17, 13, 18, 23], 13)
		self.assertEqual(res, [3, 5])

	def test_list_range_13(self):
		res = twosum([2, 5, 1, 7, 12, 6, 4, 18, 4, 9, 13, 19, 16], 12)
		self.assertEqual(res, [1, 3])

	


if __name__ == "__main__":
	unittest.main();


