"""Notes on GIL (Global Interpreter Lock) with demo of CPU-bound threads not scaling."""
# The GIL allows only one Python bytecode-executing thread at a time per process.
# CPU-bound code often doesn't speed up with threading; use multiprocessing instead.
print("Read comments in this file for GIL overview.")
