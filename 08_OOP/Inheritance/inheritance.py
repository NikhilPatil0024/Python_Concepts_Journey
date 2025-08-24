"""Simple inheritance and super()."""
class Animal:
    def speak(self): return "generic sound"
class Dog(Animal):
    def speak(self): return super().speak() + " + woof"
print(Dog().speak())
