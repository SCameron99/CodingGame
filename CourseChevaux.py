import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

pwr = []
n = int(input())
for i in range(n):
    pi = int(input())
    pwr.append(pi)

d_min = 999999999
for i in range(len(pwr)):
    for j in range(len(pwr)):
        if i != j :
            if abs(pwr[i] - pwr[j]) < d_min:
                d_min = abs(pwr[i] - pwr[j])
                answer = d_min

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(answer)
