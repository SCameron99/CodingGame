import sys
import math

class Entity():
    def __init__(self, _id, _type, x, y, shieldLife, isControlled, health, nearBase, threatFor):
        self.id = _id
        self.type = _type
        self.x = x
        self.y = y
        self.shieldLife = shieldLife
        self.isControlled = isControlled
        self.health = health
        self.nearBase = nearBase
        self.threatFor = threatFor

def check_distance(x1, x2, y1, y2):
    delta_x = abs(x1-x2)
    delta_y = abs(y1-y2)
    return int(((delta_x)**2 + (delta_y)**2)**(.5))

def find_closest(entity, list):
    dist = 999999
    result = entity
    for i in list:
        d = check_distance(entity.x, i.x, entity.y, i.y)
        if d < dist:
            dist = d
            result = i
    return result

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3

if base_x == 0:
    standby1 = "MOVE 12500 5000"
    standby2 = "MOVE 5500 1500"
    standby3 = "MOVE 1500 5500"
    e_base_x = "17630"
    e_base_y = "9000"
else:
    standby1 = "MOVE 13000 5000"
    standby2 = "MOVE 11500 8000" 
    standby3 = "MOVE 15500 3500"
    e_base_x = "0"
    e_base_y = "0"

# game loop
turn = 0
while True:
    turn += 1
    hero1 = "WAIT"
    hero2 = "WAIT"
    hero3 = "WAIT"
    player_mana = 0

    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
        if i == 0:
            player_mana = mana
    entity_count = int(input())  # Amount of heros and monsters you can see

    

    monster_list = []
    my_heroes = []
    cpu_heroes = []

    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Count down until shield spell fades
        # is_controlled: Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        entity = Entity(_id, _type, x, y, shield_life, is_controlled, health, near_base, threat_for)
        if _type == 0:
            monster_list.append(entity)
        elif _type == 1:
            my_heroes.append(entity)
        elif _type == 2:
            cpu_heroes.append(entity)

    my_dangers = []
    for i in monster_list:
        if i.nearBase == 1 and i.threatFor == 1:
            my_dangers.append(i)

    my_threats = []
    for i in monster_list:
        if i.threatFor == 1:
            my_threats.append(i)

    no_ignore = []
    for i in monster_list:
        if i.threatFor != 2:
            no_ignore.append(i)

    if len(my_dangers) == 0:
        if len(my_threats) == 0:
            if len(monster_list) > 0:
                hero1 = "MOVE " + str(monster_list[0].x) + " " + str(monster_list[0].y)
            else:
                hero1 = standby1
            #hero2 = standby2
            hero3 = standby3

        elif len(my_threats) == 1:
            hero1 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
            #hero2 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
            hero3 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)

        elif len(my_threats) == 2:
            hero1 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
            #hero2 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
            hero3 = "MOVE " + str(my_threats[1].x) + " " + str(my_threats[1].y)

        elif len(my_threats) > 2:
            if player_mana > 30:
                if check_distance(my_heroes[0].x, my_threats[0].x, my_heroes[0].y, my_threats[0].y) < 2000:
                    hero1 = "SPELL CONTROL " + str(my_threats[0].id) + " " + e_base_x + " " + e_base_y
                else:
                    hero1 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y) 
                #if check_distance(my_heroes[1].x, my_threats[1].x, my_heroes[1].y, my_threats[1].y) < 2000:
                    #hero2 = "SPELL CONTROL " + str(my_threats[1].id) + " " + e_base_x + " " + e_base_y
                #else:
                    #hero2 = "MOVE " + str(my_threats[1].x) + " " + str(my_threats[1].y) 
                if check_distance(my_heroes[2].x, my_threats[2].x, my_heroes[2].y, my_threats[2].y) < 2000:
                    hero3 = "SPELL CONTROL " + str(my_threats[2].id) + " " + e_base_x + " " + e_base_y
                else:
                    hero3 = "MOVE " + str(my_threats[2].x) + " " + str(my_threats[2].y) 
            else:
                hero1 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y) 
                #hero2 = "MOVE " + str(my_threats[1].x) + " " + str(my_threats[1].y)
                hero3 = "MOVE " + str(my_threats[2].x) + " " + str(my_threats[2].y)
    else:
        if player_mana > 10:
            if check_distance(my_heroes[0].x, my_dangers[0].x, my_heroes[0].y, my_dangers[0].y) < 1100:
                hero1 = "SPELL WIND " + e_base_x + " " + e_base_y
            else:
                hero1 = "MOVE " + str(my_dangers[0].x) + " " + str(my_dangers[0].y)
            #hero2 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
            hero3 = "MOVE " + str(my_threats[0].x) + " " + str(my_threats[0].y)
        else:
            hero1 = "MOVE " + str(my_dangers[0].x) + " " + str(my_dangers[0].y) 
            #hero2 = "MOVE " + str(my_dangers[0].x) + " " + str(my_dangers[0].y) 
            hero3 = "MOVE " + str(my_dangers[0].x) + " " + str(my_dangers[0].y) 

    if player_mana > 40 and my_heroes[0].shieldLife == 0 and turn > 114:
        hero1 = "SPELL SHIELD 0" + str(my_heroes[0].id)

    #if player_mana > 130 and my_heroes[1].shieldLife == 0:
        #hero1 = "SPELL SHIELD " + str(my_heroes[1].id)

    if player_mana > 40 and my_heroes[2].shieldLife == 0 and turn > 114:
        hero3 = "SPELL SHIELD " + str(my_heroes[2].id)

    # Hero2 Algo (ID == 1)
    if turn < 15:
        hero2 = standby1
    elif turn < 100:
        target = find_closest(my_heroes[1], monster_list)
        hero2 = "MOVE " + str(target.x) + " " + str(target.y)
    else:
        if my_heroes[1].shieldLife == 0:
            hero2 = "SPELL SHIELD 1"
        else:
            for i in my_heroes:
                if i.id == 1:
                    if (base_x == 0 and (i.x < 11000 or i.y < 3000)) or (base_x == 17630 and (i.x > 5500 or i.y > 5500)):
                        hero2 = standby1
                    else:
                        target = find_closest(my_heroes[1], monster_list)
                        if target.threatFor == 2 and player_mana > 100:
                            if check_distance(my_heroes[1].x, target.x, my_heroes[1].y, target.y) < 2100:
                                hero2 = "SPELL SHIELD " + str(target.id)
                            else:
                                hero2 = "MOVE " + str(target.x) + " " + str(target.y)
                        elif player_mana > 100:
                            if check_distance(my_heroes[1].x, target.x, my_heroes[1].y, target.y) < 2100:
                                hero2 = "SPELL CONTROL " + str(target.id) + " " + e_base_x + " " + e_base_y
                            else:
                                hero2 = "MOVE " + str(target.x) + " " + str(target.y)
                        else:
                            hero2 = "MOVE " + str(target.x) + " " + str(target.y)

    
    for i in range(3):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
        if i == 0:
            print(hero1)
        elif i == 1:
            print(hero2)
        elif i == 2:
            print(hero3)
