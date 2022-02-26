import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.


# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

distance_x = light_x - initial_tx
distance_y = light_y - initial_ty

if distance_x > 0:
    d_x = "E"
    m_x = distance_x
else:
    d_x = "W"
    m_x = abs(distance_x)

if distance_y > 0:
    d_y = "S"
    m_y = distance_y
else:
    d_y = "N"
    m_y = abs(distance_y)
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    if m_x > 0:
        if m_y > 0:
            print(d_y+d_x)
            m_x = m_x-1
            m_y = m_y-1
        else:
            print(d_x)
            m_x = m_x -1
    elif m_y > 0:
        print(d_y)
        m_y = m_y-1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    
   
