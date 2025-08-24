"""Default and keyword-only arguments."""
def connect(host, port=5432, *, ssl=True):
    return f"host={host}, port={port}, ssl={ssl}"
print(connect("localhost"))
print(connect("localhost", port=3306, ssl=False))
