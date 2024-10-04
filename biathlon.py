
import random
from enum import Enum

# Variables
OPEN = 0
CLOSED = 1

Outcome = Enum('Outcome', ['MISS', 'HIT_OPEN', 'HIT_CLOSED'])

targets = []
turn = 1

def splash():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                Biathlon              \n')
    print('           a hit or miss game         ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def new_targets():
    targets = []
    for i in range(5):
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
    if get_hit():
        if (is_closed(targets[position])):
            return Outcome.HIT_CLOSED
        
        close_target(targets, position)
        return Outcome.HIT_OPEN
    
    return Outcome.MISS

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

    if (turn > 5):
        break

    target_position = int(input("Shot nr " + str(turn) + " at: "))

    if not (target_position > 5) and not (target_position < 1):
        hit = shoot(target_position - 1)

        match hit:
            case Outcome.MISS:
                print('Miss')

            case Outcome.HIT_OPEN:
                print("Hit on target " + str(target_position))

            case Outcome.HIT_CLOSED:
                print('Hit on closed target ' + str(target_position))

        turn += 1

    else:
        print("Wrong input. Redoing.")

print('You hit ' + str(targets.count(CLOSED)) + ' out of 5 targets.')