import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
data = []
output = []
code = []
dat = 0
acc = 0
k = int(input())
for i in input().split():
    input_data = int(i)
    data.append(input_data)
n = int(input())
for i in range(n):
    line_of_code = input()
    code.append(line_of_code)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
#print(data)
#print(code)

current_line = int(0)
condition = 0
x = 0 # the value that is mov
while current_line < len(code):
    if not code[current_line].startswith("#"):
        a = code[current_line].split()
        i_1 = 0
        i_2 = 1
        i_3 = 2

        if a[i_1] == "@":
            i_1 = 1
            i_2 = 2
            i_3 = 3
            code[current_line] = code[current_line].replace("@", "#")


        if a[i_1].endswith(":"): # the code starts with a label
            i_1 = 1
            i_2 = 2
            i_3 = 3

        try:
            if (a[i_1] == "+" and condition != 1) or (a[i_1] == "-" and condition != -1):
                i_1 = 10
                i_2 = 20
                i_3 = 30
        except:
            pass

        try:
            if (a[i_1] == "+" and condition == 1) or (a[i_1] == "-" and condition == -1):
                i_1 = 1
                i_2 = 2
                i_3 = 3
        except:
            pass

        try: #if there is no instructions after the label
            if a[i_1] == "mov":
                if a[i_2] == "x0":
                    x = data.pop(0)
                elif a[i_2] == "dat":
                    x = dat
                elif a[i_2] == "acc":
                    x = acc
                try:
                    x = int(a[i_2])
                except:
                    pass
    
        
                if a[i_3] == "x1":
                    output.append(x)
                elif a[i_3] == "dat":
                    dat = x
                elif a[i_3] == "acc":
                    acc = x

            if a[i_1] == "add":
                if a[i_2] == "dat":
                    acc = acc + dat
                try:
                    acc = acc + int(a[i_2])
                except:
                    pass

            if a[i_1] == "sub":
                if a[i_2] == "dat":
                    acc = acc - dat
                try:
                    acc = acc - int(a[i_2])
                except:
                    pass

            if a[i_1] == "mul":
                if a[i_2] == "dat":
                    acc = acc * dat
                try:
                    acc = acc * int(a[i_2])
                except:
                    pass

            if a[i_1] == "not":
                if acc == 0:
                    acc = 100
                else:
                    acc = 0

            if a[i_1] == "jmp":
                jump_line = 0
                for i in code:
                    j = i.split()
                    k = j[0].strip(":")
                    if a[i_2] == k:
                        current_line = jump_line -1
                    jump_line += 1

            if a[i_1] == "teq":
                if a[i_2] == "dat":
                    v = dat
                try:
                    w = int(a[i_3])
                except:
                    pass
                if v == w:
                    condition = 1
                else:
                    condition = -1

            if a[i_1] == "tgt":
                if a[i_2] == "dat":
                    v = dat
                try:
                    w = int(a[i_3])
                except:
                    pass
                if v > w:
                    condition = 1
                else:
                    condition = -1

            if a[i_1] == "tlt":
                if a[i_2] == "dat":
                    v = dat
                try:
                    w = int(a[i_3])
                except:
                    pass
                if v < w:
                    condition = 1
                else:
                    condition = -1

            if a[i_1] == "tcp":
                if a[i_2] == "dat":
                    v = dat
                try:
                    w = int(a[i_3])
                except:
                    pass
                if v > w:
                    condition = 1
                elif v == w:
                    condition = 0
                else:
                    condition = -1

            if a[i_1] == "dgt":
                digit = int(a[i_2])
                if digit < len(str(acc)):
                    acc = int(str(acc)[(-1)*digit-1])
                else:
                    acc = 0


        except:
            pass
    
    current_line += 1

#Printing Data
j = len(output)
c = 0
for i in output:
    if i > 999:
        i = 999
    elif i < -999:
        i = -999
    print(i, end="")
    c += 1
    if c < j:
        print(" ", end="")
    

