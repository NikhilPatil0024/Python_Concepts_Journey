"""Instance attributes vs methods."""
class Box:
    def __init__(self, w,h): self.w,self.h=w,h
    def area(self): return self.w*self.h
print(Box(3,4).area())
