import sys
import math
import numpy

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

#Adding b to create augmented matrix
input_index = 0
for i in range(size):
    row = input()
    for i in row:
        equations[input_index].append(int(i))
        input_index += 1



#My first attempt at Gauss Jordan
current_line = 0
ratio = 0
divider = 1
for i in range(size*size):
    #Pushing line with pivot = 0 to the end
    while equations[current_line][current_line] == 0:
        equations += [equations.pop(current_line)] 

    #Reducing pivot to 1
    divider = equations[current_line][current_line]
    element_checked = 0
    for j in equations[current_line]:
        equations[current_line][element_checked] = round(equations[current_line][element_checked]/divider, 3)
        element_checked += 1
    
    #print("BEFORE") #Used for debugging
    #print(current_line)

    #Putting zeros on the current column

    #for i in equations: #Debugging
        #print(i[current_line])

    line_checked = 0
    for j in equations:
        if float(equations[line_checked][current_line]) != 0 and line_checked != current_line:
            element_checked = 0
            modifier = -1*equations[line_checked][current_line]

            #print("HI " + str(line_checked)) #Debugging
            
            for k in range(size*size + 1):
                equations[line_checked][element_checked] = round(equations[line_checked][element_checked] + modifier*equations[current_line][element_checked], 3)
                element_checked += 1
        line_checked += 1
    
    #for i in equations: #Debugging
        #print(i[current_line])
        
    current_line += 1
    
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(equations)  
