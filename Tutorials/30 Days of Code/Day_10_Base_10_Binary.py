#!/bin/python3

import math
import os
import random
import re
import sys

def max_ones(n):
    binary = bin(n)[2:]
    ones = binary.split("0")
    return max(map(len, ones))

if __name__ == '__main__':
    n = int(input().strip())
    print(max_ones(n))
