"""__init__ and alternative constructors via @classmethod."""
class Color:
    def __init__(self, r,g,b):
        self.r,self.g,self.b=r,g,b
    @classmethod
    def from_hex(cls, h):
        h = h.lstrip("#")
        return cls(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))
print(Color.from_hex("#00FF7F").g)
