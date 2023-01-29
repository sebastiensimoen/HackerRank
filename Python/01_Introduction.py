if __name__ == '__main__':
    print("Hello, World!")

#####################################

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#####################################

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a+b}\n{a-b}\n{a*b}")

#####################################

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f"{a//b}\n{a/b}")

#####################################

def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap

year = int(input())
print(is_leap(year))

#####################################

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1, 1):
        print(i, end='')