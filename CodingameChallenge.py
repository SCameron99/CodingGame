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
    for i in range(third_init_input):
        fifth_input, sixth_input = [int(j) for j in input().split()]
        l.append(fifth_input)
        l.append(sixth_input)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #print(l)
    #print(first_init_input, second_init_input, third_init_input)
    if first_input == "#" and second_input == "_" and t < 10:
        print("A")
    elif first_input == "_" and second_input == "_" and t < 10:
        print("A")
    elif first_input == "_" and second_input == "#" and t < 10:
        print("A")
    else:
        print(l)
        #print("B")
        print(first_input, second_input, third_input, fourth_input)
    t += 1
