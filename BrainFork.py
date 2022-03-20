import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

char_values = {" ": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
               "Z" : -1, "Y": -2, "X": -3, "W": -4, "V": -5, "U": -6, "T": -7, "S": -8, "R": -9, "Q": -10, "P": -11, "O": -12, "N": -13}

inv_char_values = {v: k for k, v in char_values.items()}

stones_values = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " ","10": " ",
                 "11": " ", "12": " ", "13": " ", "14": " ", "15": " ", "16": " ", "17": " ", "18": " ", "19": " ", "20": " ",
                 "21": " ", "22": " ", "23": " ", "24": " ", "25": " ", "26": " ", "27": " ", "28": " ", "29": " ", "30": " "}

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
previous_stone = "30"
two_next_stone = "3"
two_previous_stone = "29"

for i in magic_phrase:
    x = char_values[i]
    a = distance_between_letter(stones_values[previous_stone], i, char_values)
    b = distance_between_letter(stones_values[current_stone], i, char_values)
    c = distance_between_letter(stones_values[next_stone], i, char_values)
    g = distance_between_letter(stones_values[two_next_stone], i, char_values)
    h = distance_between_letter(stones_values[two_previous_stone], i, char_values)

    # finding the most efficient stone
    d = abs(a) + 1
    e = abs(b)
    f = abs(c) + 1
    l = abs(g) + 2
    m = abs(h) + 2
    

    
    
    
    #Left is the best option (using a)
    if d < e and d <= f and d <= l and d <= m:
        solution += "<"

        two_next_stone = next_stone
        next_stone = current_stone
        current_stone = previous_stone
        previous_stone = two_previous_stone
        two_previous_stone = str(int(two_previous_stone) - 1)

        if two_previous_stone == "0":
            two_previous_stone = "30"
            
        for k in range(abs(a)):

            if a > 0:
                new_value_index = char_values[stones_values[current_stone]] + 1
                if new_value_index == 14:
                    new_value_index = -13
                solution += "+"
                stones_values[current_stone] = inv_char_values[new_value_index]

            elif a < 0:
                new_value_index = char_values[stones_values[current_stone]] - 1
                if new_value_index == -14:
                    new_value_index = 13
                solution += "-"
                stones_values[current_stone] = inv_char_values[new_value_index]

    #Right is the best option (using c)
    elif f < d and f < e and f <= l and f <= m:
        solution += ">"

        two_previous_stone = previous_stone
        previous_stone = current_stone
        current_stone = next_stone
        next_stone = two_next_stone
        two_next_stone = str(int(two_next_stone) + 1)
        if two_next_stone == "31":
            two_next_stone = "1"

        for k in range(abs(c)):

            if c > 0:
                new_value_index = char_values[stones_values[current_stone]] + 1
                if new_value_index == 14:
                    new_value_index = -13
                solution += "+"
                stones_values[current_stone] = inv_char_values[new_value_index]

            elif c < 0:
                new_value_index = char_values[stones_values[current_stone]] - 1
                if new_value_index == -14:
                    new_value_index = 13
                solution += "-"
                stones_values[current_stone] = inv_char_values[new_value_index]

    #Left - Left is the best option(using h)
    elif m < d and m < e and m < f and m <= l:
        solution += "<<"

        two_next_stone = next_stone
        next_stone = current_stone
        current_stone = previous_stone
        previous_stone = two_previous_stone
        two_previous_stone = str(int(two_previous_stone) - 1)

        if two_previous_stone == "0":
            two_previous_stone = "30"

        two_next_stone = next_stone
        next_stone = current_stone
        current_stone = previous_stone
        previous_stone = two_previous_stone
        two_previous_stone = str(int(two_previous_stone) - 1)

        if two_previous_stone == "0":
            two_previous_stone = "30"

        for k in range(abs(h)):

            if h > 0:
                new_value_index = char_values[stones_values[current_stone]] + 1
                if new_value_index == 14:
                    new_value_index = -13
                solution += "+"
                stones_values[current_stone] = inv_char_values[new_value_index]

            elif h < 0:
                new_value_index = char_values[stones_values[current_stone]] - 1
                if new_value_index == -14:
                    new_value_index = 13
                solution += "-"
                stones_values[current_stone] = inv_char_values[new_value_index]

    #Right - Right is the best option (using g)
    elif l < d and l < e and l < f and l < m:
        solution += ">>"

        two_previous_stone = previous_stone
        previous_stone = current_stone
        current_stone = next_stone
        next_stone = two_next_stone
        two_next_stone = str(int(two_next_stone) + 1)
        if two_next_stone == "31":
            two_next_stone = "1"

        two_previous_stone = previous_stone
        previous_stone = current_stone
        current_stone = next_stone
        next_stone = two_next_stone
        two_next_stone = str(int(two_next_stone) + 1)
        if two_next_stone == "31":
            two_next_stone = "1"

        for k in range(abs(g)):

            if g > 0:
                new_value_index = char_values[stones_values[current_stone]] + 1
                if new_value_index == 14:
                    new_value_index = -13
                solution += "+"
                stones_values[current_stone] = inv_char_values[new_value_index]

            elif g < 0:
                new_value_index = char_values[stones_values[current_stone]] - 1
                if new_value_index == -14:
                    new_value_index = 13
                solution += "-"
                stones_values[current_stone] = inv_char_values[new_value_index]
    #center is the best option
    else:

        for k in range(abs(b)):

            if b > 0:
                new_value_index = char_values[stones_values[current_stone]] + 1
                if new_value_index == 14:
                    new_value_index = -13
                solution += "+"
                stones_values[current_stone] = inv_char_values[new_value_index]

            if b < 0:
                new_value_index = char_values[stones_values[current_stone]] - 1
                if new_value_index == -14:
                    new_value_index = 13
                solution += "-"
                stones_values[current_stone] = inv_char_values[new_value_index]
    
    solution += "."




    #for j in range(abs(x)):
     #   if x > 0:
      #      solution += "+"
       # elif x < 0:
        #    solution += "-"
    #solution += ".>"

#print(d, e, f)
print(solution)
