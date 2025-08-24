"""Useful itertools recipes."""
import itertools as it
print(list(it.accumulate([1,2,3,4])))
print(list(it.permutations([1,2,3], 2)))
print(list(it.groupby("aaabbc", key=lambda ch: ch)))
