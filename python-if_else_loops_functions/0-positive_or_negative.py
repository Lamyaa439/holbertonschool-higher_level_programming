#!/usr/bin/python3
import random as ra
number = ra.randint(-10,10)
if number < 0:
    print(f"{number} is negative")
elif number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
