
import random

# Variables
OPEN = 0
CLOSED = 1

targets = []
turn = 1


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
        close_target(targets, position)
        return True
    
    return False

def get_hit():
     return(random.randint(0, 100) > 50)

def render(targets):
    print('1 2 3 4 5')
    targets_string = ''
    for n in range(len(targets)):
        if is_open(targets[n]):
            targets_string = targets_string + '○ '
        else:
            targets_string = targets_string + '● '
    print(targets_string)

targets = new_targets()

while True:
    render(targets)

    target_position = int(input("Shot nr " + str(turn) + " at: "))

    if not (target_position > 5) and not (target_position < 1):
        hit = shoot(target_position - 1)

        if (hit):
            print("Hit on target " + str(target_position))

        else:
            print("Miss")

        turn += 1

    else:
        print("Wrong input. Redoing.")