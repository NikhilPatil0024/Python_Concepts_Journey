"""random for reproducible results."""
import random
random.seed(42)
print(random.randint(1,6), random.choice(['H','T']))
