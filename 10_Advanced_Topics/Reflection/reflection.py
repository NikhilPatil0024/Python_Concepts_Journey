"""getattr/setattr/hasattr for dynamic access."""
class User:
    def __init__(self): self.name = "Ada"
u = User()
if hasattr(u, "name"):
    print(getattr(u, "name"))
    setattr(u, "name", "Grace")
    print(u.name)
