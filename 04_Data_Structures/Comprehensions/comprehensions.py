"""List/set/dict comprehensions with conditions."""
squares = [x*x for x in range(6)]
evens = {x for x in range(10) if x % 2 == 0}
mapping = {x: x*x for x in range(4)}
print(squares, evens, mapping)
