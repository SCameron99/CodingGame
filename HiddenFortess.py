import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

equations = []
equation = 0
size = int(input())

#Generating the Linear Equations System
x, y, z, w = 0, 0, 0, 0
for a in range(size):
    y = 0
    for b in range(size):
        z = 0
        equations.append([])
        for c in range(size):
            w = 0
            for d in range(size):
                if x == z or y == w:
                    equations[equation].append(int(1))
                else:
                    equations[equation].append(int(0))
                w += 1
            z += 1
        y += 1
        equation += 1
    x += 1

a = np.array(equations)

#Adding b to create augmented matrix
c = []
input_index = 0
for h in range(size):
    row = input()
    for i in row:
        
        value = 0
        for j in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if i == j:
                c.append(int(value))
                equations[input_index].append(int(value))
                input_index += 1
            value += 1
            
        
b = np.array(c)
np.reshape(b, (size*size, 1))

x = np.linalg.solve(a, b)

line_checked = 0
for i in range(size):
    answer = ""
    for j in range(size):
        if int(round(x[line_checked])) == 1:
            answer += "O"
        else:
            answer += "."
        line_checked += 1
    print(answer)
