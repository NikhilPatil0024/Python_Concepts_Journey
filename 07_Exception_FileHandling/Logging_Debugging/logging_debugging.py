"""logging and debugging basics."""
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
logging.info("This is an info message")
# Debugging: use built-in breakpoint()
def add(a,b):
    # breakpoint()  # uncomment to debug
    return a+b
print(add(2,3))
