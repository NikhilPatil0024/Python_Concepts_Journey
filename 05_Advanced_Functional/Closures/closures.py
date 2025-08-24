"""Closure capturing free variables."""
def multiplier(k):
    def mul(x):
        return x * k
    return mul
times3 = multiplier(3)
print(times3(5))
