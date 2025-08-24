"""dir(), type(), vars(), inspect."""
import inspect
class T: 
    def f(self): pass
t = T()
print(dir(t)[:5], type(t).__name__, list(vars(T).keys())[:5])
print(inspect.getsource(T.f).strip().splitlines()[0])
