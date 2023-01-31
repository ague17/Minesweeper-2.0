import os

# test_board = [["■","■","■","■","■","■","■"], ["■","■","■","■","■","■","■"],
#               ["■","■","■","■","■","■","■"], ["■","■","■","■","■","■","■"],
#               ["■","■","■","■","■","■","■"], ["■","■","■","■","■","■","■"]]

def print_pboard(pboard, debug):
    '''
    The *print_pboard* function prints the state of the board seen by the player
    to the terminal screen. It also (before printing) clears the terminal screen
    so on each turn, the new state board will be placed on top of the last one.

    :param pboard: A python 2D array containing the board's information.
    :param debug: A boolean to stop the screen from refreshing (DEBUG)
    :return: This function doesn't return any value.
    '''
    if debug:
        os.system('cls' if os.name == 'nt' else 'clear')
    x_len = len(pboard)
    y_len = len(pboard[0])
    print("MINESWEEPER 2.0\n")
    chars = "     "
    for l in range(x_len):
        chars += chr(65+l)
        chars += " "
    print(chars)
    for i in range(y_len):
        s = " "+str(i+1)+" | "
        for j in range(x_len):
            s+=str(pboard[j][i])
            s+=" "
        print(s)
    print("\n")

def sum_mines(g_board):
    x_len = len(g_board)
    y_len = len(g_board[0])
    s_board = [[0  for j in range(y_len)] for i in range(x_len)]
    for i in range(x_len):
        for j in range(y_len):
            if g_board[i][j]==1:
                s_board[i][j]=-1
                continue
            counter=0
            for i_add in [-1, 0, 1]:
                for j_add in [-1, 0, 1]:
                    if i+i_add>=0 and i+i_add<x_len and j+j_add>=0 and j+j_add<y_len:
                        counter=counter+g_board[i+i_add][j+j_add]

            s_board[i][j]=counter-g_board[i][j]
    return(s_board)

<<<<<<< HEAD
test_board_2 = [[1,1,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]]
for i in range(len(test_board_2)):
    print(test_board_2[i])
summed_board=sum_mines(test_board_2)
for i in range(len(test_board_2)):
    print(summed_board[i])
=======
# test_board_2 = [[1,1,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]]
# print_pboard(test_board_2, False)
# summed_board=sum_mines(test_board_2)
# print_pboard(summed_board, False)

def cell2coords(cell):
    '''
    The *cell2coords* function converts a cell string value, as "A3", to x,y co-
    ordinates, as 0,2.

    :param cell: A string with lenght 2 or 3, made by a character and a number.
    :return: A tuple with two integers, the x and y coords.
    '''
    x = ord(cell[0])-65
    y = int(cell[1:])-1
    return (x,y)
>>>>>>> refs/remotes/origin/main
