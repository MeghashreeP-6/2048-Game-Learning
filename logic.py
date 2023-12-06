
import random

def start_game():
    # Assuming GUI to be 4*4 matrix:
    #initialize empty list. This list holds [[2], [0], [4],[8]] 
    # i points row count. 
    empty_list = []
    for i in range(4):
        empty_list.append([0] * 4)

    # Print controls
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    # Random cells will be filled with number 2
    add_list(empty_list)
    return empty_list

def add_list(add_2_to_grid):
    add_2_to_grid = random.randint()
