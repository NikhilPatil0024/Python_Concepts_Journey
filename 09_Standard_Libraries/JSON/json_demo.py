"""JSON encode/decode."""
import json
data = {"name":"Ada","langs":["Python","C"]}
s = json.dumps(data)
back = json.loads(s)
print(s, back)
