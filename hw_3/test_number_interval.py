# Задание 2.

# Разработайте и протестируйте метод numberInInterval,
# который проверяет, попадает ли переданное число в интервал (25;100).

import unittest
from number_interval import numver_interval


class TestUser(unittest.TestCase):
    def test_in_interval(self):
        self.assertTrue(numver_interval(26))

    def test_not_in_interval(self):
        self.assertFalse(numver_interval(1))

    def test_error(self):
        self.assertEqual(numver_interval('n'), 'Введено неверное значение')


if __name__ == '__main__':
    unittest.main()
