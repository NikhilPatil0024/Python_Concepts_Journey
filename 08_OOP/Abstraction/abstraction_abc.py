"""Abstract base classes (ABC)."""
from abc import ABC, abstractmethod
class Repo(ABC):
    @abstractmethod
    def get(self, key): ...
class MemRepo(Repo):
    def __init__(self): self.store={}
    def get(self,key): return self.store.get(key, None)
print(MemRepo().get("x"))
