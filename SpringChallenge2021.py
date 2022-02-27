import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class GameTile():
    def __init__(self, index, richness):
        self.index = index
        self.richness = richness

class Tree():
    def __init__(self, index, size, owner, dormant):
        self.index = index
        self.size = size
        self.owner = owner
        self.dormant = dormant

def list_my_trees(list_of_tree): #Returns a list of player owned lv3 tress
    return_list = []
    for i in list_of_tree:
        if i.owner == 1:
            return_list.append(i)
    return return_list
        
game_tiles = []
trees = []

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    game_tile = GameTile(index, richness)
    game_tiles.append(game_tile)

# game loop
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

    turn_complete = False

    for i in my_trees:
        if i.size == 3 and i.dormant == 0 and not turn_complete:
            print("COMPLETE " + str(i.index))
            turn_complete = True

    for i in my_trees:
        if i.size == 2 and i.dormant == 0 and not turn_complete:
            print("GROW "+ str(i.index))
            turn_complete = True
            
    for i in my_trees:
        if i.size == 1 and i.dormant == 0 and not turn_complete:
            print("GROW " + str(i.index))
            turn_complete = True


    
    
            



    
