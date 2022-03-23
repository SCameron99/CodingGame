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


x = 0 # the value that is mov
for i in range(len(code)):
    a = code[i].split()
    if a[0] == "mov":
        if a[1] == "x0":
            x = data.pop(0)
        elif a[1] == "dat":
            x = dat
        elif a[1] == "acc":
            x = acc
        try:
            x = int(a[1])
        except:
            pass
        

        if a[2] == "x1":
            output.append(x)
        elif a[2] == "dat":
            dat = x
        elif a[2] == "acc":
            acc = x

    if a[0] == "add":
        if a[1] == "dat":
            acc = acc + dat

    if a[0] == "sub":
        if a[1] == "dat":
            acc = acc - dat



#Printing Data
j = len(output)
c = 0
for i in output:
    print(i, end="")
    c += 1
    if c < j:
        print(" ", end="")
    

