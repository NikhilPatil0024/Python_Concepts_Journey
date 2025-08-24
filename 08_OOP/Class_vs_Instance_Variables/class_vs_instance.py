"""Class vars shared vs instance vars per-object."""
class C:
    shared = []
    def __init__(self): self.mine = []
a,b = C(), C()
a.shared.append(1); a.mine.append(1)
print(a.shared, b.shared, a.mine, b.mine)
