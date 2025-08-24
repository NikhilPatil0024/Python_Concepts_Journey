"""Iterator protocol: __iter__ and __next__."""
class Countdown:
    def __init__(self, start): self.n = start
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1
for x in Countdown(3):
    print(x)
