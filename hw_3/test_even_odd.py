# *Задание 1.

# Напишите тесты, покрывающие на 100% метод evenOddNumber, 
# который проверяет, является ли переданное число четным или нечетным

import unittest
from even_odd import even_odd


class TestUser(unittest.TestCase):
    def test_even(self):
        self.assertTrue(even_odd(10))

    def test_odd(self):
        self.assertFalse(even_odd(3))

    def test_even_odd_type_error(self):
        self.assertEqual(even_odd('m'), 'Введено неверное значение')


if __name__ == '__main__':
    unittest.main()
