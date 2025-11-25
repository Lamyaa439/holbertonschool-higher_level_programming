#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = number_str[-1]
int_last_digit = int(last_digit)
if int_last_digit > 5:
    print(f"Last digit of {number} is {int_last_digit} and is greater than 5")
elif int_last_digit < 6 and int_last_digit != 0:
    print(f"Last digit of {number} is {int_last_digit} and is less than 6 and not 0")
elif int_last_digit == 0:
    print(f"Last digit of {number} is {int_last_digit} and is 0")
