
from user import User


class UserRepository():
    def __init__(self):
        self._user_list = []

    def __str__(self) -> str:
        return f'{self.get_user_list()}'

    def get_user_list(self) -> list:
        for user in self._user_list:
            return user

    def add_user(self, user: User) -> None:
        if user.is_authentificate:
            self._user_list.append(user)
            return True
        else:
            return 'Пользователь не прошел аутентификацию'
            # raise RuntimeError('Пользователь не прошел аутентификацию')
