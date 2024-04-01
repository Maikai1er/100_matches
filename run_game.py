import time

from pull_the_match import Matches


def run_game():
    print('Welcome to the 100 matches game!')
    time.sleep(1)
    print('The rules are simple:')
    time.sleep(1)
    print('There are 100 matches in the pile')
    time.sleep(1)
    print('The players make their moves one by one')
    time.sleep(1)
    print('During each move the player has the right to pull 1 to 10 matches')
    time.sleep(1)
    print('First player to draw the last match wins!')
    matches = Matches()
