import time


def play_game():
    matches_left = 100
    while matches_left > 0:
        print("Player 1, how many matches do you want to pull out?")
        time.sleep(1)
        matches_to_draw = int(input())
        time.sleep(1)
        matches_left -= matches_to_draw
        if matches_left == 0:
            print("Player 1 wins!")
        print(f'There are {matches_left} matches left.')
        print("Player 2, how many matches do you want to pull out?")
        time.sleep(1)
        matches_to_draw = int(input())
        time.sleep(1)
        matches_left -= matches_to_draw
        if matches_left == 0:
            print("Player 2 wins!")
        print(f'There are {matches_left} matches left.')
