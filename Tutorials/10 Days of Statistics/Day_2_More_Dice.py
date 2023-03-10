# Task
# In a single toss of 2 fair (evenly-weighted) six-sided dice, 
# find the probability that the values rolled by each die will be different 
# and the two dice have a sum of 6.

dice1,dice2 = [x for x in range(1,7)],[x for x in range(1,7)]

def cross(set1, set2):
    result = []
    for i in set1:
        for j in set2:
                result.append((i, j))
    return result
dice1xdice2 = cross(dice1, dice2)

print(dice1xdice2)

count = 0
for x in dice1xdice2:
    if x[0] + x[1] == 6 and x[0] != x[1]:
        count += 1
probability = count / len(dice1xdice2)

print("{:.2f}".format(probability))
