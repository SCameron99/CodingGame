import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

first_init_input = int(input())
second_init_input = int(input())
third_init_input = int(input())

# game loop
l = []
t = 0
while True:
    first_input = input()
    second_input = input()
    third_input = input()
    fourth_input = input()
    # print(first_input, second_input, third_input, fourth_input)
    ene = 1
    for i in range(third_init_input):
        fifth_input, sixth_input = [int(j) for j in input().split()]
        if ene == 2 or ene == 5:
            l.append(fifth_input)
            l.append(sixth_input)
        ene += 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if t < 25:
        if third_input == "_":
            print("D")
        elif fourth_input == "_":
            print("E")
        elif first_input == "_":
            print("C")
        elif second_input == "_":
            print("A")
    elif t < 50:
        if fourth_input == "_":
            print("E")
        elif first_input == "_":
            print("C")
        elif second_input == "_":
            print("A")
        elif third_input == "_":
            print("D")
    elif t < 75:
        if first_input == "_":
            print("C")
        elif second_input == "_":
            print("A")
        elif third_input == "_":
            print("D")
        elif fourth_input == "_":
            print("E")
    elif t < 100:
        if second_input == "_":
            print("A")
        elif third_input == "_":
            print("D")
        elif fourth_input == "_":
            print("E")
        elif first_input == "_":
            print("C")
    #print(l)
    #print(first_init_input, second_init_input, third_init_input)
    #if first_input == "#" and second_input == "_" and t < 3:
    #    print("E")
    #elif first_input == "_" and second_input == "_" and t < 3:
    #    print("C")
    #elif first_input == "_" and second_input == "#" and t < 3:
    #    print("D")
    
    #else:
        #print(l)
        #print("E")
        #print(first_input, second_input, third_input, fourth_input)
    t += 1
