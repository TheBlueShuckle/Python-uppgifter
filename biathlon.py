
import random

# Variables
OPEN = 0
CLOSED = 1

targets = []


def splash():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                Biathlon              \n')
    print('           a hit or miss game         ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def new_targets():
    targets = []
    for _ in range(5):
        targets.append(OPEN)
    return targets

def is_open(target):
    # returnerar True om goal == open (0), annars False
    return target == OPEN

def is_closed(target):
    # returnerar True om goal == closed (1), annars False
    return target == CLOSED

def close_target(targets, position):
    targets[position] = CLOSED

def shoot(position):
    if is_open(targets[position]) and get_hit():
        close_target[targets[position]]
        return True
    
    return False

def get_hit():
     return(random.randint(0, 100) > 50)