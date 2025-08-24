"""Reference counting + cyclic GC overview."""
a = []
b = a
print("ref example:", a is b)
