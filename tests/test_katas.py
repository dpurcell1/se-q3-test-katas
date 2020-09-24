import unittest
import katas
import random


class TestKatas(unittest.TestCase):
    def test_add(self):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        result = a + b
        self.assertEqual(katas.add(a, b), result)
        self.assertEqual(katas.add(a, b), result)
        self.assertEqual(katas.add(a, b), result)
        self.assertEqual(katas.add(a, b), result)

    def test_multiply(self):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        result = a * b
        self.assertEqual(katas.multiply(a, b), result)
        self.assertEqual(katas.multiply(a, b), result)
        self.assertEqual(katas.multiply(a, b), result)
        self.assertEqual(katas.multiply(a, b), result)

    def test_power(self):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        result = a ** b
        self.assertEqual(katas.power(a, b), result)
        self.assertEqual(katas.power(a, b), result)
        self.assertEqual(katas.power(a, b), result)
        self.assertEqual(katas.power(a, b), result)

        self.assertRaises(ValueError, katas.power, 5, -2)
        self.assertRaises(ValueError, katas.power, 10, .5)

    def test_factorial(self):
        factorial_list = [1, 2, 6, 24, 120,
                          720, 5040, 40320, 362880, 3628800,
                          39916800, 479001600, 6227020800,
                          87178291200, 1307674368000]
        factor = 1
        for result in factorial_list:
            self.assertEqual(katas.factorial(factor), result)
            factor += 1

        self.assertRaises(ValueError, katas.factorial, -1)

    def test_fibonacci(self):
        fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                          377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
                          28657, 46368, 75025, 121393, 196418, 317811, 514229]
        for i in range(1, len(fibonacci_list)):
            self.assertEqual(katas.fibonacci(i), fibonacci_list[i])

        self.assertRaises(ValueError, katas.fibonacci, -1)


if __name__ == '__main__':
    unittest.main()
