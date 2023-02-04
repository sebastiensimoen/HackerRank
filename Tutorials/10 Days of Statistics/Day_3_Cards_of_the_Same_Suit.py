"""
Task
You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?
"""

suits = ['spades', 'hearts', 'clubs', 'diamonds']
card_values = ['2','3','4','5','6','7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = []
for suit in suits:
    for value in card_values:
        deck.append((suit, value))

two_card_combinations = []
for i in range(len(deck)):
    for j in range(i+1, len(deck)):
        two_card_combinations.append((deck[i], deck[j]))

print(two_card_combinations)

wished_event = 0
for combination in two_card_combinations:
    if combination[0][0] == combination[1][0]:
        wished_event += 1

print(wished_event/len(two_card_combinations)) # evaluates to 12/51
