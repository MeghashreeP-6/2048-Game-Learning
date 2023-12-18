
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

    ##Test
    print("Test")
    for i in matrix:
        print(i)
        

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
    matrix[0][3] = 2048

    #Test
    game_state(matrix)
    reverse(matrix)
    transpose(matrix)

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
        return 'lose'
    
def reverse(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix.append(matrix[i][len(matrix)-j-1])
            #print(new_matrix)
    return new_matrix

def transpose(matrix):
    new_transpose_matrix = []
    for i in range(len(matrix)):
        new_transpose_matrix.append([])
        for j in range(len(matrix)):
            new_transpose_matrix.append(matrix[j][i])
    return new_transpose_matrix
    
    #Test        
    for i in new_transpose_matrix:
        print(i)

      
start_game(4)
    