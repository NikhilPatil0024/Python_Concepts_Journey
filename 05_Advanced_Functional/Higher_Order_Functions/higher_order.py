"""Functions that accept/return functions."""
def apply_twice(f, x):
    return f(f(x))
def inc(x): return x+1
print(apply_twice(inc, 3))
