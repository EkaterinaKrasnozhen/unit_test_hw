from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
    def testDrive(self):
        self._speed = 60
        
    def park(self):
        self._speed = 0
        
    def get_company(self):
        return self._company
    
    def get_model(self):
        return self._model
    
    def get_year_release(self):
        return self._year_release
    
    def get_num_wheels(self):
        return self._num_wheels
    
    def get_speed(self):
        return self._speed
        
    def __repr__(self):
        return f'Car({self._company}, {self._model}, {self._year_release})'
        
        