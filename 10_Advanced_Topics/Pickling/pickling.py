"""Serialization with pickle."""
import pickle
data = {"x":[1,2,3]}
blob = pickle.dumps(data)
restored = pickle.loads(blob)
print(restored)
