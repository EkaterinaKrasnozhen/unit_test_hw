from Motocycle import Motocycle
from Car import Car
from Vehicle import Vehicle
import unittest
from unittest.mock import patch


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('toyota', 'rav4', 2018, 4)
        self.motocycle = Motocycle('bmv', '32v4', 2020, 2)
        
    # Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор isinstance)
    def test_isinstance(self):
        self.assertEqual(isinstance(self.car, Vehicle), True)


    #Проверить, что объект Car создается с 4-мя колесами.
    #Проверить, что объект Motorcycle создается с 2-мя колесами.
    def test_num_wheels(self):
        self.assertEqual(self.car.get_num_wheels(), 4)
        self.assertAlmostEqual(self.motocycle.get_num_wheels(), 2)
        
    
    #Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    #Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
    def test_drive(self):
        self.car.testDrive()
        self.motocycle.testDrive()
        self.assertEqual(self.car.get_speed(), 60)
        self.assertEqual(self.motocycle.get_speed(), 75)
        
    
    # Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина 
    # останавливается (speed = 0).
    # Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) 
    # мотоцикл останавливается (speed = 0).
    def test_park(self):
        self.car.testDrive()
        self.motocycle.testDrive()
        self.car.park()
        self.motocycle.park()
        self.assertEqual(self.car.get_speed(), 0)
        self.assertEqual(self.motocycle.get_speed(), 0)
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()