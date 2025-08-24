"""Demonstrate iterable vs iterator with a custom iterator."""
data = [1,2,3]          # iterable
it = iter(data)         # iterator
print(next(it), next(it), next(it))
