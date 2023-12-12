
import random

def start_game(n):
    #Create Matrix
    matrix = []
    for i in range(n):
        matrix.append([0] * n)

    #To Begin game add "2" in two random places
    matrix = add_2(matrix)
    matrix = add_2(matrix)

    ##Test
    # for i in matrix:
    #     print(i)

    return matrix

def add_2(matrix) :
    ## Original code
    # #Select random cell to place "2"
    row = random.randint(0, len(matrix)-1)
    coloumn = random.randint(0, len(matrix)-1)

    #Checking for availability. If the chosen cell is not empty, select random cell to place "2"
    while matrix[row][coloumn] != 0:
        row = random.randint(0, len(matrix)-1)
        coloumn = random.randint(0, len(matrix)-1)

    #Place "2" in the selected cell    
    matrix[row][coloumn] = 2

    ##Test
    #matrix[0][3] = 2048

    return matrix

def game_state(matrix):
    #Winning Condition
    for i in range(len(matrix)):
        #Test
        #print("i", matrix[i])
        for j in range(len(matrix)):
            #Test
            #print("j", matrix[j])
            if matrix[i][j] == 2048:
                return 'Win!'
        
        #Checking game not over condition. i.e Checking for any zero entries
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    return 'Not Over'
        
        

            


start_game(4)
    