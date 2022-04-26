import sys
import math

class Monster():
    def __init__(self, id, x, y, nearBase, threatFor):
        self.id = id
        self.x = x
        self. y = y
        self.nearBase = nearBase
        self.threatFor = threatFor



# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3

# game loop
while True:

    hero1 = "WAIT"
    hero2 = "WAIT"
    hero3 = "WAIT"

    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see

    
    monster_list = []
    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        monster = Monster(_id, x, y, near_base, threat_for)
        monster_list.append(monster)

    my_threats = []
    for i in monster_list:
        if i.threatFor == 1:
            my_threats.append(i)

    if len(my_threats) == 0:
        hero1 = "WAIT"
        hero2 = "WAIT"
        hero3 = "WAIT"

    elif len(my_threats) == 1:
        hero1 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
        hero2 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
        hero3 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)

    elif len(my_threats) == 2:
        hero1 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
        hero2 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
        hero3 = "MOVE " + str(my_threats[1].x) + " " + str(my_threats[1].y)

    elif len(my_threats) > 2:
        hero1 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
        hero2 = "MOVE " + str(my_threats[1].x) + " " + str(my_threats[1].y)
        hero3 = "MOVE " + str(my_threats[2].x) + " " + str(my_threats[2].y)

    stand = ["MOVE 70 700", "MOVE 550 100", "MOVE 450 450"]
    for i in range(len(stand)):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
        if i == 0:
            print(hero1)
        elif i == 1:
            print(hero2)
        elif i == 2:
            print(hero3)
