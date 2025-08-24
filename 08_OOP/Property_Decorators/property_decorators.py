"""@property for computed attributes with validation."""
class Celsius:
    def __init__(self, temp=0): self._temp = temp
    @property
    def temp(self): return self._temp
    @temp.setter
    def temp(self, value):
        if value < -273.15: raise ValueError("below absolute zero")
        self._temp = value
c = Celsius(25); c.temp = 30; print(c.temp)
