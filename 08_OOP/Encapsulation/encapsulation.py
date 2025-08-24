"""Name-mangling and property for controlled access."""
class Account:
    def __init__(self, balance): self.__balance = balance
    @property
    def balance(self): return self.__balance
    def deposit(self, amt): self.__balance += amt
acc = Account(100); acc.deposit(50); print(acc.balance)
