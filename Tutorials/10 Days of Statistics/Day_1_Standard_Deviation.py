# ------------ Day 1: Standard Deviation ------------

import math
import os
import random
import re
import sys

# Complete the 'stdDev' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    # Calculate the mean of the array elements
    array_mean = sum(arr) / len(arr)
    variance = sum((x - array_mean) ** 2 for x in arr) / len(arr)
    return math.sqrt(variance)

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    output = stdDev(vals)
    print("{:.1f}".format(output))
    
### WITH STATISTIC ###

import math

def stdDev(arr):
    array_mean = sum(arr) / len(arr)
    variance = sum((x - array_mean) ** 2 for x in arr) / len(arr)
    return math.sqrt(variance)

if __name__ == '__main__':
    n = int(input().strip()
    vals = list(map(int, input().rstrip().split()))
    output = stdDev(vals)
    print("{:.1f}".format(output))
