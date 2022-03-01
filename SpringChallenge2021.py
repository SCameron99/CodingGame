import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class GameTile():
    def __init__(self, index, richness, neigh0, neigh1, neigh2, neigh3, neigh4, neigh5):
        self.index = index
        self.richness = richness
        self.neigh0 = neigh0
        self.neigh1 = neigh1
        self.neigh2 = neigh2
        self.neigh3 = neigh3
        self.neigh4 = neigh4
        self.neigh5 = neigh5

class Tree():
    def __init__(self, index, size, owner, dormant):
        self.index = index
        self.size = size
        self.owner = owner
        self.dormant = dormant


def list_my_trees(list_of_tree): #Returns a list of player owned lv3 tress
    return_list = []
    for i in list_of_tree:
        if i.owner == 1 and i.size != 0:
            return_list.append(i)
    return return_list
        
def count_my_seeds(list_of_tree):
    seed_list = []
    count = 0
    for i in list_of_tree:
        if i.size == 0 and i.owner == 1:
            count += 1
            seed_list.append(i)
    return count, seed_list

def count_tree(list_of_tree, size):
    tree_list = []
    count = 0
    for i in list_of_tree:
        if i.size == size:
            count += 1
            tree_list.append(i)
    return count, tree_list

def find_best_neighbour(tree_index, game_tiles, tree_list): #Returns the index of the neigh with most richness
    max_richness = 0
    cell_index = 99
    for i in game_tiles: #i is the index of the source tree
        if tree_index == i.index:
            for j in game_tiles: 
                if j.index == i.neigh0 or j.index == i.neigh1 or j.index == i.neigh2 or j.index == i.neigh3 or j.index == i.neigh4 or j.index == i.neigh5:
                    occupied = False
                    for k in tree_list:
                        if k.index == j.index:
                            occupied = True
                    if not occupied and j.richness > max_richness:
                        cell_index = j.index
                        max_richness = j.richness
    return cell_index

def find_best_neighbour2(tree_index, game_tiles): #Returns the index of the neigh with most richness
    max_richness = 0
    cell_index = 99
    for i in game_tiles: #i is the index of the source tree
        if tree_index == i.index:
            for j in game_tiles: 
                if j.index == i.neigh0 or j.index == i.neigh1 or j.index == i.neigh2 or j.index == i.neigh3 or j.index == i.neigh4 or j.index == i.neigh5:
                    if j.richness > max_richness:
                        cell_index = j.index
                        max_richness = j.richness
    return cell_index



game_tiles = []
trees = []

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    game_tile = GameTile(index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5)
    game_tiles.append(game_tile)

# game loop

modifier = 0

while True:
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees
    
    trees = []
    my_trees = []

    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        tree = Tree(cell_index, size, is_mine, is_dormant)
        trees.append(tree)

    number_of_possible_actions = int(input())  # all legal actions

    for i in range(number_of_possible_actions):
        possible_action = input()  # try printing something from here to start with

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>

    
    my_trees = list_my_trees(trees)
    seed_number, my_seeds = count_my_seeds(trees)
    seed_cost = seed_number

    lvl1_number, my_lvl1 = count_tree(my_trees, 1)
    lvl1_cost = lvl1_number + 1

    lvl2_number, my_lvl2 = count_tree(my_trees, 2)
    lvl2_cost = lvl2_number + 3

    lvl3_number, my_lvl3 = count_tree(my_trees, 3)
    lvl3_cost = lvl3_number + 7

    turn_complete = False

    #EXPAND VS GROW MODIFIER (0 = EXPAND, 2 = GROW)
    if day < 8:
        modifier = 0
    elif 8 <= day <= 15:
        modifier = 1
    elif day > 15:
        modifier = 2

    #PRIORITY 3 LVL3
    if len(my_lvl3) >= 3:
        for i in my_lvl3:
            if not turn_complete:
                print("COMPLETE " + str(i.index))
                turn_complete = True
                
    #PRIORITY DAY23
    if day == 23:
        for i in my_lvl3:
            if not turn_complete:
                print("COMPLETE " + str(i.index))
                turn_complete = True
    
    
    #PRIORITY FREE SEED
    if seed_number == 0 and not turn_complete:
        dest = find_best_neighbour(my_trees[0].index, game_tiles, trees)
        print("SEED " + str(my_trees[0].index) + " " + str(dest))
        turn_complete = True

    #PRIORITY LV3 CHEAPER THAN LVL2
    if lvl3_cost <= (lvl2_cost + 3*modifier)and not turn_complete:
        if sun >= lvl3_cost:
            for i in my_lvl2:
                if i.dormant == 0 and not turn_complete:
                    print("GROW " + str(i.index))
                    turn_complete = True

    #PRIORITY LV2 CHEAPER THAN LVL1
    if lvl2_cost <= (lvl1_cost + 2*modifier) and not turn_complete:
        if sun >= lvl2_cost:
            for i in my_lvl1:
                if i.dormant == 0 and not turn_complete:
                    print("GROW " + str(i.index))
                    turn_complete = True

    #PRIORITY LV1 CHEAPER THAN SEED
    if lvl1_cost <= (seed_cost + 1*modifier) and not turn_complete:
        if sun >= lvl1_cost:
            for i in my_seeds:
                if i.dormant == 0 and not turn_complete:
                    print("GROW " + str(i.index))
                    turn_complete = True
    elif not turn_complete:
        if sun >= seed_cost:
            if len(my_lvl3) > 0:
                for i in my_lvl3:
                    if i.dormant == 0 and not turn_complete:
                        best_neigh = find_best_neighbour2(i.index, game_tiles)
                        best_2neigh = find_best_neighbour2(best_neigh, game_tiles)
                        dest = find_best_neighbour(best_2neigh, game_tiles, trees)
                        if dest != 99:
                            print("SEED " + str(i.index) + " " + str(dest))
                            turn_complete = True
            if len(my_lvl2) > 0 and not turn_complete:
                for i in my_lvl2:
                    if i.dormant == 0 and not turn_complete:
                        best_neigh = find_best_neighbour2(i.index, game_tiles)
                        dest = find_best_neighbour(best_neigh, game_tiles, trees)
                        if dest != 99:
                            print("SEED " + str(i.index) + " " + str(dest))
                            turn_complete = True
            if len(my_lvl1) > 0 and not turn_complete:
                for i in my_lvl1:
                    if i.dormant == 0 and not turn_complete:
                        dest = find_best_neighbour(i.index, game_tiles, trees)
                        if dest != 99:
                            print("SEED " + str(i.index) + " " + str(dest))
                            turn_complete = True

    #TODO
    #PRIORITISE GROW IN RICH SOIL
    #
    

    

    if not turn_complete:
        print("WAIT")


    
    
            



    
