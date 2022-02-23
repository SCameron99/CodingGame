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

class Zombie():
    """
    Zombie Class
    """
    def __init__(self, id, x, y, next_x, next_y):
        """
        Args:
            id: zombie Id
            x: zombie_x
            y: zombie_y
            next_x : next x position
            next_y : next y position
        """
        self.id = id
        self.x = x
        self.y = y
        self.next_x = next_x
        self.next_y = next_y

def calculate_distance(x1, x2, y1, y2):
    """
    Args:
        x1:
        x2:
        y1:
        y2:
    returns a floatof the distance between 2 points.
    """
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)
    distance = math.sqrt(dist_x**2 + dist_y**2)
    return distance

def target_closest(x, y, target_list):
    """
    Args:
        x : player x position
        y : player y position
        target_list: a list of possible target
    returns: a set of coordinates
    """
    min_distance = 50000
    target_x = 0
    target_y = 0 
    for i in target_list:
        target_distance = calculate_distance(x, i.x, y, i.y)
        if target_distance < min_distance:
            min_distance = target_distance
            target_x = i.x
            target_y = i.y
    return target_x, target_y




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
    zombie_list = []
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombie = Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext)
        zombie_list.append(zombie)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    dest_x, dest_y = target_closest(x, y, human_list)

    print(str(dest_x) + " " + str(dest_y))
