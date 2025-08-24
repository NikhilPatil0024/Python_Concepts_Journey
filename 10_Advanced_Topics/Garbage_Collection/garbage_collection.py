"""Manual interaction with gc module."""
import gc
print("Enabled:", gc.isenabled())
collected = gc.collect()
print("Collected objects:", collected)
