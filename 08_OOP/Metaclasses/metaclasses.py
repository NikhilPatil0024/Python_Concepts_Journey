"""Simple metaclass to auto-register subclasses."""
registry = {}
class Registrar(type):
    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        if name != "Base": registry[name] = cls
        return cls
class Base(metaclass=Registrar): pass
class A(Base): pass
class B(Base): pass
print(sorted(registry.keys()))
