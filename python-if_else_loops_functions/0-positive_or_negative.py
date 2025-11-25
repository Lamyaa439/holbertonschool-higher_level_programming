#!/usr/bin/python3
import random as ra
number = ra.randint(-100, 100)
if number < 0:
    print(f"{number} is negative")
if number > 0:
    print(f"{number} is positive")
if number == 0:
    print(f"{number} is zero")
