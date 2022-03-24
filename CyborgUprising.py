import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories
distances = {}
for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    distances[i] = {'factory_1': factory_1, 'factory_2': factory_2, 'distance': distance}

def end_turn(movements):
    print(movements)

# ONE Factory Mode
def one_factory():
    movements = str("WAIT")
    for factory in my_factories:
        source = str(my_factories[factory]['entity_id'])

        # Low Production
        if (my_factories[factory]['arg_3'] < 2):
            if (my_factories[factory]['arg_2'] > 10):
                movements = movements + ";INC " + str(source)

        # Medium or High Production
        if (my_factories[factory]['arg_3'] == 2 or my_factories[factory]['arg_3'] == 3):
            if (my_factories[factory]['arg_2'] > 5):
                target,force = find_closest_target(source)
                force = force + 1
                movements = movements + ";MOVE " + str(source) + " " + str(target) + " " + str(force)
    end_turn(movements)

def find_closest_target(source):
    short_link = 21
    target = 2
    force = 1
    for distance in distances:
        if (str(distances[distance]['factory_1']) == source):
            if distances[distance]['distance'] < short_link:
                for factory in neutral_factories:
                    if (neutral_factories[factory]['entity_id'] == distances[distance]['factory_2']):
                        short_link = distances[distance]['distance']
                        target = distances[distance]['factory_2']
    for enemy in neutral_factories:
        if (neutral_factories[enemy]['entity_id'] == target):
            force = neutral_factories[enemy]['arg_2']
    return target,force

# game loop
while True:
    my_factories = {}
    enemy_factories = {}
    neutral_factories = {}
    my_troops = {}
    enemy_troops = {}
    entity_count = int(input())  # the number of entities (e.g. factories and troops)

    
    # separates entities into sub categories
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])
        
        if (entity_type == "FACTORY" and arg_1 == 1):
            my_factories[entity_id] = {'entity_id': entity_id, 'arg_1': arg_1, 'arg_2': arg_2, 'arg_3': arg_3}
        elif (entity_type == "FACTORY" and (arg_1 == 0)):
            neutral_factories[entity_id] = {'entity_id': entity_id, 'arg_1': arg_1, 'arg_2': arg_2, 'arg_3': arg_3}
        elif (entity_type == "FACTORY" and (arg_1 == -1)):
            enemy_factories[entity_id] = {'entity_id': entity_id, 'arg_1': arg_1, 'arg_2': arg_2, 'arg_3': arg_3}
        elif (entity_type == "TROOP" and arg_1 == 1):
            my_troops[entity_id] = {'entity_id': entity_id, 'arg_1': arg_1, 'arg_2': arg_2, 'arg_3': arg_3, 'arg_4': arg_4, 'arg_5': arg_5}
        elif (entity_type == "TROOP" and arg_1 == -1):
            enemy_troops[entity_id] = {'entity_id': entity_id, 'arg_1': arg_1, 'arg_2': arg_2, 'arg_3': arg_3, 'arg_4': arg_4, 'arg_5': arg_5}

    
    factory_count = len(my_factories) + len(neutral_factories) + len(enemy_factories)

    # choosing game mode
    if (len(my_factories) > 0):
        one_factory()

    


    # for factory in my_factories:
    #    if (my_factories[factory]['arg_2'] > 8): #and (my_factories[factory]['arg_3'] == 3)
          #or (my_factories[factory]['arg_2'] > 15) and (my_factories[factory]['arg_3'] == 2)
          #or (my_factories[factory]['arg_2'] > 10) and (my_factories[factory]['arg_3'] == 1)
          #or (my_factories[factory]['arg_2'] > 0) and (my_factories[factory]['arg_3'] == 0)):
    #        attacker = factory
    #        distance_cible1 = 21
    #        size_1 = my_factories[factory]['arg_2']*3//10
    #        for enemy in enemy_factories:
    #            for distance in distances:
    #                if ((distances[distance]['factory_1'] == my_factories[factory]['entity_id'])
    #                and (distances[distance]['factory_2'] == enemy_factories[enemy]['entity_id'])
    #                and (distances[distance]['distance'] < distance_cible1)):
    #                    distance_cible1 = distances[distance]['distance']
    #                    cible_1 = enemy_factories[enemy]['entity_id']
    #                    size_1 = enemy_factories[enemy]['arg_2']+1
    #                elif ((distances[distance]['factory_2'] == my_factories[factory]['entity_id'])
    #                and (distances[distance]['factory_1'] == enemy_factories[enemy]['entity_id'])
    #                and (distances[distance]['distance'] < distance_cible1)):
    #                    distance_cible1 = distances[distance]['distance']
    #                    cible_1 = enemy_factories[enemy]['entity_id']
    #                    size_1 = enemy_factories[enemy]['arg_2']+1
    #        if not (attacker == cible_1):
    #            movements = movements + ";MOVE " + str(attacker) + " " + str(cible_1) + " " + str(size_1)
    #        distance_cible3 = 21
    #        for enemy in enemy_factories:
    #            for distance in distances:
    #                if ((distances[distance]['factory_1'] == my_factories[factory]['entity_id'])
    #                and (distances[distance]['factory_2'] == enemy_factories[enemy]['entity_id'])
    #                and (distances[distance]['distance'] < distance_cible3)
    #                and (enemy_factories[enemy]['entity_id'] != cible_1)):
    #                    distance_cible3 = distances[distance]['distance']
    #                    cible_3 = enemy_factories[enemy]['entity_id']
    #                    size_3 = enemy_factories[enemy]['arg_2']+1
    #                elif ((distances[distance]['factory_2'] == my_factories[factory]['entity_id'])
    #                and (distances[distance]['factory_1'] == enemy_factories[enemy]['entity_id'])
    #                and (distances[distance]['distance'] < distance_cible3)
    #                and (enemy_factories[enemy]['entity_id'] != cible_1)):
    #                    distance_cible3 = distances[distance]['distance']
    #                    cible_3 = enemy_factories[enemy]['entity_id']
    #                    size_3 = enemy_factories[enemy]['arg_2']+1
    #        if not (attacker == cible_3):
    #            movements = movements + ";MOVE " + str(attacker) + " " + str(cible_3) + " " + str(size_1)
    #        distance_cible2 = 21
    #        size_2 = (my_factories[factory]['arg_2'] // 6)
    #        for enemy in neutral_factories:
    #            for distance in distances:
    #                if ((distances[distance]['factory_1'] == my_factories[factory]['entity_id'])
    #                and (distances[distance]['factory_2'] == neutral_factories[enemy]['entity_id'])
    #                and (distances[distance]['distance'] < distance_cible2)):
    #                    distance_cible2 = distances[distance]['distance']
    #                    cible_2 = neutral_factories[enemy]['entity_id']
    #                elif ((distances[distance]['factory_2'] == my_factories[factory]['entity_id'])
    #                and (distances[distance]['factory_1'] == neutral_factories[enemy]['entity_id'])
    #                and (distances[distance]['distance'] < distance_cible2)):
    #                    distance_cible2 = distances[distance]['distance']
    #                    cible_2 = neutral_factories[enemy]['entity_id']
    #        if not (attacker == cible_2):
    #            movements = movements + ";MOVE " + str(attacker) + " " + str(cible_2) + " " + str(1)

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #max_score = -1
    #target = -1
    #for i in neutral_factories:
    #    if (int(neutral_factories[i]['arg_3']) == 3):
    #        target = (int(neutral_factories[i]["entity_id"]))
    #        break
    #    elif (int(neutral_factories[i]['arg_3']) == 2):
    #        target = (int(neutral_factories[i]["entity_id"]))
    #        break
    #for i in neutral_factories:
    #    score = 0
    #    score = score + (int(neutral_factories[i]['arg_3'])*3)
    #    if (score > max_score):
    #        max_score = score
    #        target = (int(neutral_factories[i]["entity_id"]))
    
    #for i in enemy_factories:
    #    score = 0
    #    score = score + (int(enemy_factories[i]['arg_3']*4))
    #    if (score > max_score):
    #        max_score = score
    #        target = (int(enemy_factories[i]["entity_id"]))

    #if (target == -1):
    #    for i in neutral_factories:
    #        if (int(neutral_factories[i]['arg_3']) == 1):
    #            target = (int(neutral_factories[i]["entity_id"]))
    #            break
    #        elif (int(neutral_factories[i]['arg_3']) == 0):
    #            target = (int(neutral_factories[i]["entity_id"]))
    #            break

    #if (target == -1):
    #    for i in enemy_factories:
    #        if (int(enemy_factories[i]['arg_3']) == 1):
    #            target = (int(enemy_factories[i]["entity_id"]))
    #            break
    #        elif (int(enemy_factories[i]['arg_3']) == 0):
    #            target = (int(enemy_factories[i]["entity_id"]))
    #            break

    #size = 3
    #source = -1
    #most_cyborgs = -1
    #for i in my_factories:
    #    cyborgs = (int(my_factories[i]['arg_2']))
    #    if (cyborgs > most_cyborgs):
    #        most_cyborgs = cyborgs
    #        source = (int(my_factories[i]['entity_id']))
    #        size = int((int(my_factories[i]['arg_2']))/2)

    #if (source == -1 or target == -1):
    #    print("WAIT") 
    #else:
    #    print("MOVE " + str(source) + " " + str(target) + " " + str(size))
    


   

    # Write an action using print
    # To debug: 
    #print("Debug messages...", file=sys.stderr, flush=True)


    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
    #print("WAIT")
