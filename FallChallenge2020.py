import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Action():
    def __init__(self, action_id, action_type, delta_0, delta_1, delta_2, delta_3, price):
        self.action_id = action_id
        self.action_type = action_type
        self.delta_0 = delta_0
        self.delta_1 = delta_1
        self.delta_2 = delta_2
        self.delta_3 = delta_3
        self.price = price



# game loop
while True:
    actions = []
    action_count = int(input())  # the number of spells and recipes in play
    for i in range(action_count):
        inputs = input().split()
        action_id = int(inputs[0])  # the unique ID of this spell or recipe
        action_type = inputs[1]  # in the first league: BREW; later: CAST, OPPONENT_CAST, LEARN, BREW
        delta_0 = int(inputs[2])  # tier-0 ingredient change
        delta_1 = int(inputs[3])  # tier-1 ingredient change
        delta_2 = int(inputs[4])  # tier-2 ingredient change
        delta_3 = int(inputs[5])  # tier-3 ingredient change
        price = int(inputs[6])  # the price in rupees if this is a potion
        tome_index = int(inputs[7])  # in the first two leagues: always 0; later: the index in the tome if this is a tome spell, equal to the read-ahead tax; For brews, this is the value of the current urgency bonus
        tax_count = int(inputs[8])  # in the first two leagues: always 0; later: the amount of taxed tier-0 ingredients you gain from learning this spell; For brews, this is how many times you can still gain an urgency bonus
        castable = inputs[9] != "0"  # in the first league: always 0; later: 1 if this is a castable player spell
        repeatable = inputs[10] != "0"  # for the first two leagues: always 0; later: 1 if this is a repeatable player spell
        action = Action(action_id, action_type, delta_0, delta_1, delta_2, delta_3, price)
        actions.append(action)

    for i in range(2):
        # inv_0: tier-0 ingredients in inventory
        # score: amount of rupees
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    for i in actions:
        if (inv_0 + i.delta_0) >= 0 and (inv_1 + i.delta_1) >= 0 and (inv_2 + i.delta_2) >= 0 and (inv_3 + i.delta_3) >= 0 and i.price > 10:
            print("BREW " + str(i.action_id))
            break

    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
