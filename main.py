from __future__ import annotations
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def deposite(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("insufficient funds")


# account = BankAccount()
# import sys

# for line in sys.stdin:
#     parts = line.strip().split()
#     if not parts:
#         continue
#     cmd = parts[0]
#     if cmd == "deposit":
#         account.deposite(int(parts[1]))
#     elif cmd == "withdraw":
#         account.withdraw(int(parts[1]))
#     elif cmd == "balance":
#         print(account.balance)


# class Shape:
#     def area(self):
#         return 0


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side**2


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * (self.radius**2)


# kind = input()
# num = float(input())
# if kind == "square":
#     shape = Square(num)
# elif kind == "circle":
#     shape = Circle(num)
# print(shape.area())


# class Vector:
#     def __init__(self, x, y):
#         self.x = int(x)
#         self.y = int(y)

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"


# x1, y1 = input().split()
# x2, y2 = input().split()
# v1 = Vector(x1, y1)
# v2 = Vector(x2, y2)
# print(v1 + v2)


# limit = int(input())


# def fibonacci(limit):
#     prev = 1
#     cur = 0
#     while cur < limit:
#         yield cur
#         tmp = cur
#         cur = prev + cur
#         prev = tmp


# print(" ".join(map(str, fibonacci(limit))))

# n = int(input())
# print(sum(x**2 for x in range(1, n + 1)))

# from functools import wraps


# a = int(input())
# b = int(input())


# def logged(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(f"called {func.__name__}: {res}")
#         return res

#     return wrapper


# @logged
# def add(a, b):
#     return a + b


# add(a, b)

# import re


# n = int(input())
# pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
# for _ in range(n):
#     text = input()
#     if re.fullmatch(pattern, text):
#         print("valid")
#     else:
#         print("invalid")

# import json

# try:
#     data = json.loads(input())
#     print(data.get("name", "not found"))
# except json.JSONDecodeError:
#     print("invalid json")

import sys

inventory: dict[str, int] = {}
for line in sys.stdin:
    parts = line.strip().split()
    cmd = parts[0]
    if cmd == "add":
        item, quantity = parts[1], int(parts[2])
        inventory[item] = inventory.get(item, 0) + quantity
    elif cmd == "remove":
        item, quantity = parts[1], int(parts[2])
        if not item in inventory:
            print("error: not found")
        elif inventory[item] < quantity:
            print("error: insufficient")
        else:
            inventory[item] -= quantity
            if inventory[item] == 0:
                del inventory[item]
    elif cmd == "search":
        item = parts[1]
        print(inventory.get(item, 0))
    elif cmd == "list":
        if not inventory:
            print("empty")
        else:
            for k in sorted(inventory.keys()):
                print(f"{k}: {inventory[k]}")
