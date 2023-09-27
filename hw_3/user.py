class User:
    def __init__(self, name:str, surname:str, login: str, password: str) -> None:
        self._name = name
        self._surname = surname
        self._login = login
        self._password = password
        self._is_authentificate = False
    
    def authentificate(self, login: str, password: str) -> bool:
        self._is_authentificate = self._login == login and self._password == password
        return self._is_authentificate
    
    def __str__(self) -> str:
        return f'{self.name} {self.surname}'
    
    @property
    def login(self):
        return self._login
    
    @property
    def password(self):
        return self._password
    
    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def is_authentificate(self):
        return self._is_authentificate