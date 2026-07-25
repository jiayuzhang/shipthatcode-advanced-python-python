class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient funds")


account = BankAccount()
import sys

for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    cmd = parts[0]
    if cmd == "deposit":
        account.deposite(int(parts[1]))
    elif cmd == "withdraw":
        account.withdraw(int(parts[1]))
    elif cmd == "balance":
        print(account.balance)
