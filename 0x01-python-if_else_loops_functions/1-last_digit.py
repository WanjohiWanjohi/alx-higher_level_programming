#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
my_digit = abs(number) % 10
if number < 0:
    my_digit = -my_digit
print(f"Last digit of {number:d} is {my_digit:d} and is ", end="")
if my_digit > 5:
    print("greater than 5")
elif my_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
