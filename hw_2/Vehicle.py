from abc import ABC, abstractmethod, abstractproperty


class Vehicle(ABC):
    def __init__(self, company, model, year_release, num_wheels):
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = num_wheels
        self._speed = 0
    
    @abstractmethod
    def testDrive():
        pass
    
    @abstractmethod
    def park():
        pass
    
    