import sys
import math

# Save humans, destroy zombies!

class Human():
    """
    human class
    """
    def __init__(self, id, x, y):
        """
        Args:
            id : human_id
            x : human_x
            y : human_y
        """
        self.id = id
        self.x = x
        self.y = y

# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    human_list = []
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        human = Human(human_id, human_x, human_y)
        human_list.append(human)
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    print(str(human_list[-1].x) + " " + str(human_list[-1].y))

