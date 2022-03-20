import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

char_values = {" ": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
               "Z" : -1, "Y": -2, "X": -3, "W": -4, "V": -5, "U": -6, "T": -7, "S": -8, "R": -9, "Q": -10, "P": -11, "O": -12, "N": -13}

inv_char_values = {v: k for k, v in char_values.items()}

stones_values = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " ","10": " ",
                 "11": " ", "12": " ", "13": " ", "14": " ", "15": " ", "16": " ", "17": " ", "18": " ", "19": " ", "20": " ",}

def distance_between_letter(letter_1, letter_2, letter_values):
    x = letter_values[letter_1]
    y = letter_values[letter_2]
    dist = y-x
    if dist > 13:
        dist = -(27-dist)
    elif dist < -13:
        dist = 27+dist
    return dist
magic_phrase = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

solution = ""
current_stone = "1"
next_stone = "2"
previous_stone = "20"

for i in magic_phrase:
    x = char_values[i]
    a = distance_between_letter(stones_values[previous_stone], i, char_values)
    b = distance_between_letter(stones_values[current_stone], i, char_values)
    c = distance_between_letter(stones_values[next_stone], i, char_values)

    # finding the most efficient stone

    d = abs(a) + 1
    e = abs(b)
    f = abs(c) + 1
    
    #Left is the best option (using a)
    if d < e and d < f:
        solution += "<"

        next_stone = current_stone
        current_stone = previous_stone
        previous_stone = str(int(previous_stone) - 1)
        if previous_stone == "0":
            previous_stone = "20"
            
        for k in range(abs(a)):
            if a > 0:
                new_value_index = char_values[stones_values[current_stone]] + 1
                if new_value_index == 14:
                    new_value_index = -13
                solution += "+"
                stones_values[current_stone] = inv_char_values[new_value_index]



    for j in range(abs(x)):
        if x > 0:
            solution += "+"
        elif x < 0:
            solution += "-"
    solution += ".>"
print(solution)
