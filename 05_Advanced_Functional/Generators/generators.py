"""Generators and generator expressions."""
def gen():
    for i in range(3):
        yield i*i
print(list(gen()))
print(list(i*i for i in range(3)))
