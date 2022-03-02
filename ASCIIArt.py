import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(h):
    row = input()
    for ch in t:
        valid_letter = False
        for letter in alphabet:
            if letter == ch.casefold():
                letter_index = alphabet.index(letter)
                print(row[l*letter_index:l*letter_index+l], end="")
                valid_letter = True
        if not valid_letter:        
            print(row[26*l:27*l], end="")
    print("")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print('')
