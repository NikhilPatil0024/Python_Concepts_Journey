"""Arithmetic, comparison, assignment, identity, membership."""
x = 5
x += 2
print(x, 5 == 5, 3 != 2, 3 < 5, 7 in [1,2,7])
a = []
b = a
print(a is b, a is not [])
