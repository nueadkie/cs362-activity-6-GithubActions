import unittest
import calculator


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calculator.subtract(4, 2), 2)

    def test_mult(self):
        self.assertEqual(calculator.multiply(7, 5), 35)

    def test_div(self):
        self.assertEqual(calculator.divide(9, 3), 3)


if __name__ == "__main__":
    unittest.main()
