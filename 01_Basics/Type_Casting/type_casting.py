"""Safe conversions between basic types."""
s = "123"
i = int(s)
f = float(s)
s2 = str(456)
b = bool(0)      # False because 0 is falsy

print(i, f, s2, b)
