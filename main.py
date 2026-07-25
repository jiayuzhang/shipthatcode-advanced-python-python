class BankAccount:
    def __init__(self):
        self.balance = 0
    # Implement deposit, withdraw

account = BankAccount()
import sys
for line in sys.stdin:
    parts = line.strip().split()
    if not parts:
        continue
    cmd = parts[0]
    # Handle the three commands
