import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

char_values = {" ": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
               "Z" : -1, "Y": -2, "X": -3, "W": -4, "V": -5, "U": -6, "T": -7, "S": -8, "R": -9, "Q": -10, "P": -11, "O": -12, "N": -13}

stones_values = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " ","10": " ",
                 "11": " ", "12": " ", "13": " ", "14": " ", "15": " ", "16": " ", "17": " ", "18": " ", "19": " ", "20": " ",}

def distance_between_letter(letter_1, letter_2, letter_values):
    x = letter_values[letter_1]
    y = letter_values[letter_2]
    dist = abs(x-y)
    if dist > 13:
        dist = 27-dist
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
    for j in range(abs(x)):
        if x > 0:
            solution += "+"
        elif x < 0:
            solution += "-"
    solution += ".>"
print(solution)
