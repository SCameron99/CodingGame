import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, pwr = int(input()), []
for i in range(n):
    pwr.append(int(input()))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(np.min(np.diff(np.sort(np.array(pwr)))))
