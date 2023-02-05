"""
Task
The ratio of boys to girls for babies born in Russia is 1:1.09. 
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
Write a program to compute the answer using the above parameters. 
Then print your result, rounded to a scale of 3 decimal places (i.e., 1.123 format).
"""

from math import comb

def binomial_distribution(n, k, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

ratio = tuple(map(float, input().split()))
p_boy = ratio[0] / sum(ratio)
p_girl = ratio[1] / sum(ratio)

result = sum(binomial_distribution(6, i, p_boy) for i in range(3, 7))

print("{:.3f}".format(result))
