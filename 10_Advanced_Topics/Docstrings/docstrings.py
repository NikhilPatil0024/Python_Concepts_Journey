"""Docstrings and help()."""
def add(a: int, b: int) -> int:
    """Return the sum of a and b.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b
print(add.__doc__.strip().splitlines()[0])
