# Unit tests
import unittest
from MyPackage import cap


# In order to create a Test class, you need to inherit
# from the unittest.TestCase class (OOP inheritance)
class TestCap(unittest.TestCase):

    # Test the cap_test function with one word
    def test_one_word(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")

    # Test the cap_test function with multiple words
    def test_multi_word(self):
        text = "i love coding"
        result = cap.cap_text(text)
        self.assertEqual(result, "I Love Coding")


if __name__ == '__main--':
    unittest.main()
