"""Dictionaries: key->value mappings."""
d = {"name": "Ada", "lang": "Python"}
d["year"] = 1991
print(d.get("name"), list(d.keys()), list(d.values()))
