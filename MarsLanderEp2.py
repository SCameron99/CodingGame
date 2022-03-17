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
    previous_y = land_y
    previous_x = land_x

landing_zone.append(first_x)
landing_zone.append(last_x)

print(landing_zone)

#print(last_x)
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
    print("-20 3")
