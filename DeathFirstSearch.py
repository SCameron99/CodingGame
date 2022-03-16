import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
vertice_list = []
gateway_list = []
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    vertice_list.append([n1, n2])
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateway_list.append(ei)

hi_score = 0
for g in gateway_list:
    score = 0
    for v in vertice_list:
        if ((int(v[0]) == int(g)) or (int(v[1]) == int(g))):
            score = score+1
    if (score > hi_score):
        hi_score = score
        largest_gateway = g

hi_score = 0
for g in gateway_list:
    score = 0
    second_gateway = 999
    for v in vertice_list:
        if ((int(v[0]) == int(g)) or (int(v[1]) == int(g))):
            if (int(g) != int(largest_gateway)):
                score = score+1
    if (score > hi_score):
        hi_score = score
        if (int(g) != int(largest_gateway)):
            second_gateway = g
old_pos = 0
first_turn = True
# game loop
while True:

    #print(second_gateway)
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    output = False
    for vert in vertice_list:
        if not output:
            if ((int(vert[0]) == si and vert[1] in gateway_list) or 
            (int(vert[1]) == si and vert[0] in gateway_list)): # Priority 1 Agent next to gateway
                output = True
                x = vert[0]
                y = vert[1]
                vertice_list.remove(vert)
                print(f"{x} {y}")

    if (len(gateway_list) > 1):


        

        

        #Largest Gateway
        if not first_turn:
            for vert in vertice_list:
                if not output:
                    if (int(vert[0]) == si):
                        possible_move = int(vert[1])
                        for v in vertice_list:
                            if (((int(v[0]) == int(possible_move)) and (int(v[1]) == int(largest_gateway))) or 
                            ((int(v[1]) == int(possible_move)) and (int(v[0]) == int(largest_gateway)))):
                                output = True
                                x = vert[0]
                                y = vert[1]
                                vertice_list.remove(vert)
                                print(f"{x} {y}")
                    elif (int(vert[1]) == si):
                        possible_move = int(vert[0])
                        for v in vertice_list:
                            if (((int(v[0]) == int(possible_move)) and (int(v[1]) == int(largest_gateway))) or 
                            ((int(v[1]) == int(possible_move)) and (int(v[0]) == int(largest_gateway)))):
                                output = True
                                x = vert[0]
                                y = vert[1]
                                vertice_list.remove(vert)
                                print(f"{x} {y}")
        #Second Gateway
            for vert in vertice_list:
                if not output:
                    if (int(vert[0]) == si):
                        possible_move = int(vert[1])
                        for v in vertice_list:
                            if (((int(v[0]) == int(possible_move)) and (int(v[1]) == int(second_gateway))) or 
                            ((int(v[1]) == int(possible_move)) and (int(v[0]) == int(second_gateway)))):
                                output = True
                                x = vert[0]
                                y = vert[1]
                                vertice_list.remove(vert)
                                print(f"{x} {y}")
                    elif (int(vert[1]) == si):
                        possible_move = int(vert[0])
                        for v in vertice_list:
                            if (((int(v[0]) == int(possible_move)) and (int(v[1]) == int(second_gateway))) or 
                            ((int(v[1]) == int(possible_move)) and (int(v[0]) == int(second_gateway)))):
                                output = True
                                x = vert[0]
                                y = vert[1]
                                vertice_list.remove(vert)
                                print(f"{x} {y}")

        #Largest Gateway 3 Steps
        for vert in vertice_list:
            if not output:
                if (int(vert[0]) == si):
                    possible_move = int(vert[1])
                    for v in vertice_list:
                        if (int(v[0]) == possible_move):
                            move_2 = int(v[1])
                            for u in vertice_list:
                                if (((int(u[0]) == int(move_2)) and (int(u[1]) == int(largest_gateway))) or 
                                ((int(u[1]) == int(move_2)) and (int(u[0]) == int(largest_gateway)))):
                                    output = True
                                    x = u[0]
                                    y = u[1]
                                    vertice_list.remove(u)
                                    print(f"{x} {y}")
                        elif (int(v[1]) == possible_move):
                            move_2 = int(v[0])
                            for u in vertice_list:
                                if (((int(u[0]) == int(move_2)) and (int(u[1]) == int(largest_gateway))) or 
                                ((int(u[1]) == int(move_2)) and (int(u[0]) == int(largest_gateway)))):
                                    output = True
                                    x = u[0]
                                    y = u[1]
                                    vertice_list.remove(u)
                                    print(f"{x} {y}")
                elif (int(vert[1]) == si):
                    possible_move = int(vert[0])
                    for v in vertice_list:
                        if (int(v[0]) == possible_move):
                            move_2 = int(v[1])
                            for u in vertice_list:
                                if (((int(u[0]) == int(move_2)) and (int(u[1]) == int(largest_gateway))) or 
                                ((int(u[1]) == int(move_2)) and (int(u[0]) == int(largest_gateway)))):
                                    output = True
                                    x = vert[0]
                                    y = vert[1]
                                    vertice_list.remove(vert)
                                    print(f"{x} {y}")
                        elif (int(v[1]) == possible_move):
                            move_2 = int(v[0])
                            for u in vertice_list:
                                if (((int(u[0]) == int(move_2)) and (int(u[1]) == int(largest_gateway))) or 
                                ((int(u[1]) == int(move_2)) and (int(u[0]) == int(largest_gateway)))):
                                    output = True
                                    x = vert[0]
                                    y = vert[1]
                                    vertice_list.remove(vert)
                                    print(f"{x} {y}")

        
        

        

        

        

    

    

    for vert in vertice_list:
        if not output:
            if ((int(vert[0]) == si) or (int(vert[1]) == si) and 
            (int(vert[0]) != old_pos) and (int(vert[1]) != old_pos)):
                output = True
                x = vert[0]
                y = vert[1]
                vertice_list.remove(vert)
                print(f"{x} {y}")

            #elif ((int(vert[0]) == si) or (int(vert[1]) == si)):
            #    output = True
            #    x = vert[0]
            #    y = vert[1]
            #    vertice_list.remove(vert)
            #    print(f"{x} {y}")
    first_turn = False
    old_pos = int(si)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    #print(vertice_list)
