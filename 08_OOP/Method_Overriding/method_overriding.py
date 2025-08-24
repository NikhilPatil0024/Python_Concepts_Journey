"""Child overrides parent method."""
class Base:
    def greet(self): return "base"
class Child(Base):
    def greet(self): return "child"
print(Child().greet())
