#!/usr/bin/env python3

# The signatures of this class is required for the automated grading to work.
# You must not change its name.
# You must add the correct signatures for each missing method as outlined
# in the task instructions.
class BankAccount:
    def __init__(self, _owner, _balance=0.0):
        self._owner = _owner
        self._balance = _balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        elif self._balance - amount < 0:
            raise ValueError("Insufficient funds")
        else:
            self._balance -= amount

    def __str__(self):
        return f"Account owner: {self._owner}\nAccount balance: CHF {self._balance}"

    def __repr__(self):
        return f"BankAccount('{self._owner}', {self._balance})"
    
    # implement the necessary methods

# The following lines call the functionality
# This way you can check what it does.

my_account = BankAccount("Melon Tusk", 269800000000)
my_account.withdraw(200000000000)
print(my_account)
print(repr(my_account))