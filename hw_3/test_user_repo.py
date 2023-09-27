# Добавьте класс UserRepository для управления пользователями. В этот класс должен быть включен метод
# addUser, который добавляет пользователя в систему, если он прошел аутентификацию. Покройте тестами новую
# функциональность

import unittest
from user import User
from user_repository import UserRepository


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('Kate', 'Krasnozhen', 'login', 'password')
        self.repo = UserRepository()

    def test_add_user_success(self):
        self.user.authentificate('login', 'password')
        self.assertTrue(self.repo.add_user(self.user))

    def test_add_user_failed_no_login(self):
        self.user.authentificate('', 'password')
        # self.assertRaisesRegex(RuntimeError, 'Пользователь не прошел аутентификацию', self.repo.add_user, user=self.user)
        self.assertEqual(self.repo.add_user(self.user),
                         'Пользователь не прошел аутентификацию')

    def test_add_user_failed_no_password(self):
        self.user.authentificate('log', '')
        # self.assertRaisesRegex(RuntimeError, 'Пользователь не прошел аутентификацию', self.repo.add_user, user=self.user)
        self.assertEqual(self.repo.add_user(self.user),
                         'Пользователь не прошел аутентификацию')

    def test_add_user_failed_no_log_password(self):
        self.user.authentificate('', '')
        # self.assertRaisesRegex(RuntimeError, 'Пользователь не прошел аутентификацию', self.repo.add_user, user=self.user)
        self.assertEqual(self.repo.add_user(self.user),
                         'Пользователь не прошел аутентификацию')

    def test_user_list(self):
        self.user.authentificate('login', 'password')
        self.repo.add_user(self.user)
        self.assertEqual(self.repo.get_user_list(), self.user)


if __name__ == '__main__':
    unittest.main()
