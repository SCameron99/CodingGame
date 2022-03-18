import sys
import math

# Save the Planet.
# Use less Fossil Fuel.
previous_y = 3000
previous_x = -1
first_x = -1
last_x = -1
landing_zone = [] #2 elements, first_x and last_x
n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

    if previous_y == land_y:
        first_x = previous_x
        last_x = land_x
        landing_height = land_y
    previous_y = land_y
    previous_x = land_x

landing_zone.append(first_x)
landing_zone.append(last_x)


first_turn = True
angle = 0
speed = 2
# game loop
while True:
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # R P. R is the desired rotation angle. P is the desired thrust power.

    #Determining starting position
    if x < landing_zone[0] and first_turn:
        side = "left"
        first_turn = False
    elif x > landing_zone[1]:
        side = "right"
        first_turn = False
    else:
        side = "center"
        first_turn = False

    #Determining maximum horizontal speed
    if x < landing_zone[0]:
        max_hs = 50
        min_hs = 27
        if landing_zone[0] - x < 250:
            max_hs = 15
            min_hs = 5
    elif x > landing_zone[1]:
        max_hs = -27
        min_hs = -50
        if x - landing_zone[1] < 250:
            max_hs = -5
            min_hs = -15
    else:
        min_hs = -15
        max_hs = 15


    #Determining Angle
    if hs > max_hs:
        angle = 25
        if landing_zone[0] < x < landing_zone[1]:
            angle = 45 
    elif hs < min_hs:
        angle = -25
        if landing_zone[0] < x < landing_zone[1]:
            angle = -45
    else:
        angle = 0

    if hs < -50:
        angle = -40
        if landing_zone[0] < x < landing_zone[1]:
            angle = -50
    elif hs > 50:
        angle = 40
        if landing_zone[0] < x < landing_zone[1]:
            angle = 50

    #Vertical Speed
    if vs < -30:
        speed = "4"
    elif vs < -25:
        speed = "3"
    elif vs < -15:
        speed = "2"
    else:
        speed = "1"

    if angle > 10 or angle < -10:
        speed = "4"

    #High Plateau scenario
    if x > landing_zone[1]:
        if x - landing_zone[1] > y - landing_height:
            if hs < -50:
                angle = 0
                speed = "4"
            else:
                angle = 26
                speed = "4"
    elif x < landing_zone[0]:
        if landing_zone[0] -x > y -landing_height:
            if hs > 50:
                angle = 0
                speed = "4"
            else:
                angle = -26
                speed = "4"

    print(str(angle) + " " + str(speed))



    
