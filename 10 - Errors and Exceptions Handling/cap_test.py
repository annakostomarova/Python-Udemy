import unittest
import cap # just CAP since they both in same locatin with cap_test

class TestCap(unittest.TestCase):
	"""this class inherits from unittest.TestCase"""

	def test_one_word(self):
		text = 'test'
		result = cap.cap_text(text)
		self.assertEqual(result,"Test")

	def test_multi_word(self):
		text = 'lets test python'
		result = cap.cap_text(text)
		self.assertEqual(result,"Lets Test Python")

if __name__ == '__main__':
	unittest.main()

