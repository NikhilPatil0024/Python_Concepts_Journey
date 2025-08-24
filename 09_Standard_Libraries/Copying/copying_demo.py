"""Shallow vs deep copy."""
import copy
a = [[1,2],[3,4]]
b = copy.copy(a)      # shallow
c = copy.deepcopy(a)  # deep
a[0][0] = 99
print(a, b, c)
