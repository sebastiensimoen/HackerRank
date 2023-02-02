import math
import os
import random
import re
import sys

# Complete the 'weightedMean' function below.
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W

def weightedMean(X, W):
    # Write your code here
    number_weights = sum(W)  
    weighted_sum = sum([v * w for v, w in zip(X, W)])
    weighted_mean = weighted_sum / number_weights
    return "{:.1f}".format(weighted_mean)

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    result = weightedMean(vals, weights)
    print(result)
