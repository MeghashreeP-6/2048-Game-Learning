import random
import constants as c

def start_game(n):
    #Create Matrix
    matrix = []
    for i in range(n):
        matrix.append([0] * n)

    #To Begin game add "2" in two random places
    matrix = add_2(matrix)
    matrix = add_2(matrix)

    #compress(matrix)

    ##Test
    # print("Test")
    # for i in matrix:
    #     print(i)

    return matrix

def add_2(matrix) :
    #Select random cell to place "2"
    row = random.randint(0, len(matrix)-1)
    coloumn = random.randint(0, len(matrix)-1)

    #Checking for availability. If the chosen cell is not empty, select random cell to place "2"
    while matrix[row][coloumn] != 0:
        row = random.randint(0, len(matrix)-1)
        coloumn = random.randint(0, len(matrix)-1)

    #Place "2" in the selected cell    
    matrix[row][coloumn] = 2  

    return matrix    
    ##Test
    # matrix[0][0] = 2
    # matrix[0][1] = 2
    # matrix[1][2] = 2
    # matrix[2][0] = 4

    # print("ADD")
    # for i in matrix:
    #     print(i)
     
    #Test
    # game_state(matrix)
    #reverse(matrix)
    #transpose(matrix)
    #compress(matrix)
    #merge(matrix, False)
    #move_up(matrix)
    #return matrix
    #move_down(matrix)
    #move_left(matrix)
    #move_right(matrix)

#Getting the game status
def game_state(matrix):
    #Winning Condition
    for i in range(len(matrix)):
        #Test
        #print("i", matrix[i])
        for j in range(len(matrix)):
            #Test
            #print("j", matrix[j])
            if matrix[i][j] == 2048:
                #print("Win")
                return 'Win!'
        
        #Checking game not over condition. i.e Checking for any zero entries
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                 if matrix[i][j] == 0:
                    #print("Not Over")
                    return 'Not Over'
                
        #Checking for two identical numbers placed next to each other that can be added
        #If there are no numbers that can be added then 'Game Over'     
        for i in range(len(matrix)-1):
            for j in range(len(matrix)-1):
                if matrix[i][j]== matrix[i+1][j] or matrix[i][j+1] == matrix[i][j]:
                    #print("Not Over")
                    return 'Not Over!'

        #Checking for two identical numbers placed next to each other that can be added in the last row
        #If there are no numbers that can be added then 'Game Over' 
        for k in range(len(matrix)-1):
            # if i == len(matrix)-1:
            #     print("Not Over")
            #     break
                #return 'Not Over'
            if matrix[len(matrix)-1][k] == matrix[len(matrix)-1][k+1]:
                #print("Not Over")
                return 'Not Over!'
        
        #Checking for two identical numbers placed next to each other that can be added in the last column
        #If there are no numbers that can be added then 'Game Over' 
        for k in range(len(matrix)-1):
            # if i == len(matrix)-1:
            #     print("Not Overr")
            #     break
            if matrix[k][len(matrix)-1] == matrix[k+1][len(matrix)-1]:
                #print("Not Over")
                return 'NOt Over!'
        return 'Lost:('
    
#Reversing a matrix(Reversing content of each row)
def reverse(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[i][len(matrix)-j-1])
    # print("Reverse")
    # for i in new_matrix:
    #     print(i)
    return new_matrix

#Getting the transpose of a matrix(Interchange rows and coloumns)
def transpose(matrix):
    new_transpose_matrix = []
    for i in range(len(matrix)):
        new_transpose_matrix.append([])
        for j in range(len(matrix)):
            new_transpose_matrix[i].append(matrix[j][i])
    # print("Transpose")
    # for i in new_transpose_matrix:
    #     print(i)    
    return new_transpose_matrix

#Function to compress the grid
#after every step before and after merging cells
def compress(matrix):
    new_matrix_compress = []
    #print(len(matrix))
    for i in range(c.GRID_LEN):
        temp_matrix = []
        for j in range(c.GRID_LEN):
            temp_matrix.append(0)
        new_matrix_compress.append(temp_matrix)
    
    changed = False
    for i in range(c.GRID_LEN):
        position = 0
        for j in range(c.GRID_LEN):
            if matrix[i][j]!= 0:
                new_matrix_compress[i][position] = matrix[i][j]
                if j!=position:
                    changed = True
                position += 1
    # print("Compress")
    # for i in new_matrix_compress:
    #     print(i)
    return new_matrix_compress, changed  

#Function to merge cells
#after compressing
def merge(matrix, changed):
    #changed = False
    for i in  range(c.GRID_LEN):
        for j in range (c.GRID_LEN-1):
            if (matrix[i][j] == matrix[i][j+1] and matrix[i][j]!= 0):
                matrix[i][j] *= 2
                matrix[i][j+1]= 0
                changed = True
    # print("Merge")
    # for i in matrix:
    #     print(i)
    return matrix, changed

def up(game):
    print("Up")
    game = transpose(game)
    game, changed = compress(game)
    game, changed = merge(game, changed)
    game = compress(game)
    game = transpose(game)
    return game, changed

def down(game):
    print("Down")
    game = reverse(transpose(game))
    game, changed = compress(game)
    game, changed = merge(game, changed)
    game = compress(game)
    game = transpose(reverse(game))
    # for i in game:
    #     print(i)
    return game, changed

def left(game):
    game, changed = compress(game)
    game, changed = merge(game, changed)
    game = compress(game)
    # for i in game:
    #     print(i)
    return game, changed

def right(game):
    print("Right")
    game = reverse(game)
    game, changed = compress(game)
    game, changed = merge(game, changed)
    game = compress(game)
    game = reverse(game)
    # for i in game:
    #     print(i)
    # print(changed)
    return game, changed