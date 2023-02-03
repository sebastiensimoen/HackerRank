# ------------ Day 1: Interquartile Range ------------

import math
import os
import random
import re
import sys

# Complete the 'interQuartile' function below.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function

    arr = []
    for i, j in zip(values, freqs):
        arr.extend([i] * j)
    arr.sort()
    n = len(arr)

    def median(arr, n):
        if n % 2 == 0:
            return (arr[n//2 - 1] + arr[n//2]) / 2
        return arr[n//2]

    q2 = median(arr, n) #Median(X)
    q1_array = arr[:n//2]
    q1 = median(q1_array, len(q1_array)) #Median(L)
    if n % 2 == 0:
        q3_array = arr[n//2:]
    else:
        q3_array = arr[n//2 + 1:]
    q3 = median(q3_array, len(q3_array)) #Median(R)
    return round(float(q3 - q1), 1)


if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interquar = interQuartile(val, freq)
    print("{:.1f}".format(interquar))
    
### WITH STATISTIC ###


import statistics

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    
    arr = []
    for value, freq in zip(values, freqs):
        arr.extend([value] * freq)
    arr.sort()
    n = len(arr)

    q2 = statistics.median(arr) #Median(X)
    q1_array = arr[:n//2]
    q1 = statistics.median(q1_array) #Median(L)
    q3_array = arr[n//2 + n % 2:]
    q3 = statistics.median(q3_array) #Median(R)
    return round(float(q3 - q1), 1)

if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interquar = interQuartile(val, freq)
    print("{:.1f}".format(interquar))
