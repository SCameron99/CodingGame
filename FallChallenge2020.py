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

def get_best_potion(actions):
    best_price = 0
    best_potion = 0
    for i in actions:
        if i.action_type == "BREW" and i.price > best_price:
            best_potion = i.action_id
            best_price = i.price
    return best_potion

def return_deltas(potion_id, actions):
    delta_0, delta_1, delta_2, delta_3 = 0, 0, 0, 0
    for i in actions:
        if i.action_id == potion_id:
            delta_0, delta_1, delta_2, delta_3 = i.delta_0, i.delta_1, i.delta_2, i.delta_3
    return delta_0, delta_1, delta_2, delta_3

def find_cast(delta_index, actions):
    usable_cast = 0
    for i in actions:
        if i.action_type == "CAST":
            if delta_index == 0 and i.delta_0 > 0:
                usable_cast = i.action_id
            elif delta_index == 1 and i.delta_1 > 0:
                usable_cast = i.action_id
            elif delta_index == 2 and i.delta_2 > 0:
                usable_cast = i.action_id
            elif delta_index == 3 and i.delta_3 > 0:
                usable_cast = i.action_id
    return usable_cast




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


    inv_0, inv_1, inv_2, inv_3, = 0, 0, 0, 0
    for i in range(2):
        # inv_0: tier-0 ingredients in inventory
        # score: amount of rupees
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    best_potion = get_best_potion(actions)

    best_delta_0, best_delta_1, best_delta_2, best_delta_3, = return_deltas(best_potion, actions)
    
    if best_delta_3 + inv_3 < 0:
        to_cast = find_cast(3, actions)
        to_cast_delta_0, to_cast_delta_1, to_cast_delta_2, to_cast_delta_3, = return_deltas(to_cast, actions)
        if to_cast_delta_2 + inv_2 < 0:
            to_cast = find_cast(2, actions)
            to_cast_delta_0, to_cast_delta_1, to_cast_delta_2, to_cast_delta_3, = return_deltas(to_cast, actions)
            if to_cast_delta_1 + inv_1 < 0:
                to_cast = find_cast(1, actions)
                to_cast_delta_0, to_cast_delta_1, to_cast_delta_2, to_cast_delta_3, = return_deltas(to_cast, actions)
                if to_cast_delta_0 + inv_0 < 0:
                    to_cast = find_cast(0, actions)
                    to_cast_delta_0, to_cast_delta_1, to_cast_delta_2, to_cast_delta_3, = return_deltas(to_cast, actions)
                else:
                    print("CAST " + str(to_cast))

    

    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
