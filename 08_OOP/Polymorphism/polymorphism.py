"""Same interface, different implementations."""
class Shape:
    def area(self): raise NotImplementedError
class Rect(Shape):
    def __init__(self,w,h): self.w,self.h=w,h
    def area(self): return self.w*self.h
class Circle(Shape):
    def __init__(self,r): self.r=r
    def area(self):
        import math; return math.pi*self.r*self.r
for s in (Rect(2,3), Circle(2)):
    print(type(s).__name__, s.area())
