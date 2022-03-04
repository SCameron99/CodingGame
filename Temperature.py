import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
min_temp = 10000
temp_n = 0
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    u = abs(int(i))
    if u < min_temp:
        temp_n = t
        min_temp = u
    elif (u == min_temp) and (t != temp_n):
        temp_n = abs(temp_n)

print(temp_n)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("result")
