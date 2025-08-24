"""Truthiness and boolean operators."""
print(bool(0), bool(1), bool(""), bool("x"), bool([]), bool([0]))
x, y = True, False
print(x and y, x or y, not x)
