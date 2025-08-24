"""Type hints and mypy-friendly annotations."""
from typing import List, Dict, Optional
def greet(name: str, excited: bool = False) -> str:
    out = f"Hello, {name}"
    return out + "!" if excited else out
def squares(xs: List[int]) -> Dict[int, int]:
    return {x: x*x for x in xs}
print(greet("Nikhil", True), squares([1,2,3]))
