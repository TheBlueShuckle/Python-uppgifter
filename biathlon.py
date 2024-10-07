
import random
from enum import Enum

# Variables
OPEN = 0
CLOSED = 1

Outcome = Enum('Outcome', ['MISS', 'HIT_OPEN', 'HIT_CLOSED'])

players_targets = []
player_turns = []

def splash():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                Biathlon              \n')
    print('           a hit or miss game         ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#   Targets
def new_targets():
    targets = []
    for i in range(5):
        targets.append(OPEN)
    return targets

def is_open(target):
    return target == OPEN

def is_closed(target):
    return target == CLOSED

def close_target(targets, position):
    targets[position] = CLOSED

#   Shooting
def shoot(player, position):
    if get_hit():
        if (is_closed(players_targets[player][position])):
            return Outcome.HIT_CLOSED
        
        close_target(players_targets[player], position)
        return Outcome.HIT_OPEN
    
    return Outcome.MISS

def get_hit():
     return(random.randint(0, 100) > 50)

#   UI
def render(player_index):
    print('---')
    print('Player ' + str(player_index + 1) + '\'s turn')
    print('1 2 3 4 5')
    targets_string = ''
    for n in range(len(players_targets[player_index])):
        if is_open(players_targets[player_index][n]):
            targets_string = targets_string + '○ '
        else:
            targets_string = targets_string + '● '
    print(targets_string)

#   Start game
def init_players(total_players):
    for player in range(total_players):
        players_targets.append(new_targets())
        player_turns.append(1)


splash()
init_players(int(input('How many players are there?: ')))

for i in range(5):
    for player in range(len(players_targets)):
        shot_counted = False    # shot_counted is used for handling wrong inputs

        while not shot_counted:
            render(player)

            target_position = int(input("Shot nr " + str(player_turns[player]) + " at: "))

            if not (target_position > 5) and not (target_position < 1):     # If inputed number is between 1 and 5
                outcome = shoot(player, target_position - 1)

                match outcome:
                    case Outcome.MISS:
                        print('Miss')

                    case Outcome.HIT_OPEN:
                        print("Hit on target " + str(target_position))

                    case Outcome.HIT_CLOSED:
                        print('Hit on closed target ' + str(target_position))

                player_turns[player] += 1
                shot_counted = True

            else:
                print("Wrong input. Redoing turn.")


print('Jobs done')