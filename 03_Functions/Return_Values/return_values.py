"""Returning multiple values (tuple packing)."""
def min_max(xs):
    return min(xs), max(xs)
lo, hi = min_max([3, 1, 8])
print(lo, hi)
