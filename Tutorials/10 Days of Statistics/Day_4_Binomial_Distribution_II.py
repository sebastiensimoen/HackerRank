"""
Task
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. 
What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?
"""

from math import comb

def binomial_distribution(n, k, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

defective_percentage, batch_size = map(int, input().split())
p = defective_percentage / 100

prob_no_more_than_2 = sum(binomial_distribution(batch_size, i, p) for i in range(3))
prob_at_least_2 = 1-sum(binomial_distribution(batch_size, i, p) for i in range(2))

print("{:.3f}".format(prob_no_more_than_2))
print("{:.3f}".format(prob_at_least_2))
