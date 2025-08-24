"""Using ABCs as interfaces."""
from abc import ABC, abstractmethod
class Serializer(ABC):
    @abstractmethod
    def dumps(self, obj): ...
class JsonSerializer(Serializer):
    def dumps(self, obj):
        import json; return json.dumps(obj)
print(JsonSerializer().dumps({"x":1}))
