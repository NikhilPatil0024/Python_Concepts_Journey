"""Assertions for defensive programming."""
def sqrt(x: float) -> float:
    assert x >= 0, "x must be non-negative"
    return x ** 0.5
print(sqrt(9))
