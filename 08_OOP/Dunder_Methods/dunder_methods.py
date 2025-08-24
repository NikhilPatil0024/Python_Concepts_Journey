"""Special methods customize behavior."""
class Vec:
    def __init__(self,x,y): self.x,self.y=x,y
    def __repr__(self): return f"Vec({self.x},{self.y})"
    def __add__(self, other): return Vec(self.x+other.x, self.y+other.y)
    def __len__(self): return 2
print(Vec(1,2)+Vec(3,4), len(Vec(0,0)))
