"""@staticmethod vs @classmethod."""
class E:
    factor = 2
    @staticmethod
    def double(x): return x*2
    @classmethod
    def scale(cls, x): return x*cls.factor
print(E.double(3), E.scale(3))
