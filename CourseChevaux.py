import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

pwr = []

n = int(input())
for i in range(n):
    pi = int(input())
    pwr.append(pi)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(np.min(np.diff(np.sort(np.array(pwr)))))
