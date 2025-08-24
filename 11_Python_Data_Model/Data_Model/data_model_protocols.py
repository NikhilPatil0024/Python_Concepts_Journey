"""Data model: implementing __len__, __iter__, __contains__ gives container semantics."""
class Bag:
    def __init__(self): self._items = []
    def add(self, x): self._items.append(x)
    def __len__(self): return len(self._items)
    def __iter__(self): return iter(self._items)
    def __contains__(self, x): return x in self._items
b = Bag(); b.add(1); b.add(2)
print(len(b), list(b), 2 in b)
