"""Regular expressions with re."""
import re
m = re.findall(r"\b\w{3}\b", "one two three four five six")
print(m)
