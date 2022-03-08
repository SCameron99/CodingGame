import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

input_lines = []
output_lines = []
empty_list = []
size = int(input())
for i in range(size):
    row = input()
    input_lines.append(row)
    output_lines.append(empty_list)
    output_row = 0
    for j in range(size):
        output_lines.insert(output_row, "o")
        output_row += 1

print(output_lines)
#Clearing 0s
row_index_input = 0
for i in input_lines:
    col_index_input = 0
    for j in i:
        if j == 0:
            row_index_output = 0
            for k in output_lines:
                col_index_output = 0
                for l in k:
                    if row_index_output == row_index_input and col_index_input == col_index_output:
                        output_lines[row_index_output][col_index_output] = "."
                    col_index_output += 1
                row_index_output += 1
        col_index_input += 1
    row_index_input += 1

            

for i in range(size):

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(output_lines[i-1])
