"""
Task
There are  urns labeled X, Y, and Z.

Urn X contains 4 red balls and 3 black balls.
Urn Y contains 5 red balls and 4 black balls.
Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. What is the probability that, 3 of the  balls drawn, 2 are red and 1 is black?
"""

urn_x = ['r', 'r', 'r', 'r', 'b', 'b', 'b']
urn_y = ['r', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b']
urn_z = ['r', 'r', 'r', 'r', 'b', 'b', 'b', 'b']

combinaison = [(x, y, z) for x in urn_x for y in urn_y for z in urn_z]
print(combinaison)

matches = sum([(draw.count('r')==2 and draw.count('b')==1) for draw in combinaison])
probability = matches / len(combinaison)
print("{:.2f}".format(probability))
