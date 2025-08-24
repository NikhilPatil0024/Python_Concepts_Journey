"""Recursive example: factorial with base case and input guard."""
def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    return 1 if n in (0,1) else n * factorial(n-1)
print(factorial(5))
