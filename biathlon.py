# Variables
open = 0
closed = 1


def splash():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                Biathlon              \n')
    print('           a hit or miss game         ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def is_open(goal):
    # returnerar True om goal == open (0), annars False
    return goal == open

def is_closed(goal):
    # returnerar True om goal == closed (1), annars False
    return goal == closed

def new_targets():
    ts = []
    for _ in range(5):
        ts.append(open)
    return ts

def close_target(targets, position):
    targets[postition] = closed

