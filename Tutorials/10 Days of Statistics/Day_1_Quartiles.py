# ------------ Day 1: Quartiles ------------

import math
import os
import random
import re
import sys

# Complete the 'quartiles' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

def quartiles(arr, n):
    # Write your code here
    
    # Median(X):
    def median(arr, n):
        if n % 2 == 0:
            return (arr[n//2 - 1] + arr[n//2]) / 2
        return arr[n//2]
    
    arr = sorted(arr)
    
    # Q2 or median(X)
    q2 = median(arr, n)
    
    # Q1 or median(L)
    q1_array = []
    
    for i in arr:
        if i < q2:
            q1_array.append(i)
    q1 = median(q1_array, len(q1_array))
    # Q3 or median(U)
    q3_array = []
    for i in arr:
        if i > q2:
            q3_array.append(i)
    q3 = median(q3_array, len(q3_array))
    
    return [int(q1), int(q2), int(q3)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data, n)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()

### WITH STATISTIC ###

import statistics
import os

def quartiles(arr, n):
    arr = sorted(arr)
    q2 = statistics.median(arr)
    q1_array = [x for x in arr if x < q2]
    q1 = statistics.median(q1_array)
    q3_array = [x for x in arr if x > q2]
    q3 = statistics.median(q3_array)
    return [int(q1), int(q2), int(q3)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data, n)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
