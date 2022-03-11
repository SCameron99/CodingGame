import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
table = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext = ext.casefold()
    table[ext] = mt
for i in range(q):
    fname = input()  # One file name per line.
    fname = fname.casefold()
    key = (fname.split(".")[-1])
    if "." in fname:
        try:
            print(table[key])
        except:
            print("UNKNOWN")
    else:
        print("UNKNOWN")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

