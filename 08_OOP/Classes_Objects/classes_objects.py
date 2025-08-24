"""Defining a class and creating objects."""
class Person:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hi, I'm {self.name}"
p = Person("Ada")
print(p.greet(), p.species)
