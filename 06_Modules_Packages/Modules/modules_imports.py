"""Creating and importing a simple module (self-contained demo)."""
# In real projects, place functions in separate files and import them.
def util():
    return "from util"
if __name__ == "__main__":
    print(util())
