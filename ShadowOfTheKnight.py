import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]


min_x = 0
min_y = 0
max_x = w
max_y = h
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir == "U":
        bomb_x = x0
        max_y = y0-1                #
        bomb_y = (max_y+min_y)//2   #U
    elif bomb_dir == "UR":
        min_x = x0+1                #
        bomb_x = (min_x+max_x)//2   #R
        max_y = y0-1                #
        bomb_y = (max_y+min_y)//2   #U
    elif bomb_dir == "R":
        min_x = x0+1                #
        bomb_x = (min_x+max_x)//2   #R
        bomb_y = y0
    elif bomb_dir == "DR":
        min_x = x0+1                #
        bomb_x = (min_x+max_x)//2   #R
        min_y = y0+1                #
        bomb_y = (min_y+max_y)//2   #D
    elif bomb_dir == "D":
        bomb_x = x0
        min_y = y0+1                #
        bomb_y = (min_y+max_y)//2   #D
    elif bomb_dir == "DL":
        max_x = x0-1                #
        bomb_x = (min_x+max_x)//2   #L
        min_y = y0+1                #
        bomb_y = (min_y+max_y)//2   #D
    elif bomb_dir == "L":
        max_x = x0-1                #
        bomb_x = (min_x+max_x)//2   #L
        bomb_y = y0
    elif bomb_dir == "UL":
        max_x = x0-1                #
        bomb_x = (min_x+max_x)//2   #L
        max_y = y0-1                #
        bomb_y = (max_y+min_y)//2   #U

    x0 = int(bomb_x)
    y0 = int(bomb_y)
    print(x0,y0)






    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
