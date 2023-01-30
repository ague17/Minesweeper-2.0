import os

test_board = [["■","■","■","■","■","■","■"], ["■","■","■","■","■","■","■"], ["■","■","■","■","■","■","■"],
              ["■","■","■","■","■","■","■"], ["■","■","■","■","■","■","■"], ["■","■","■","■","■","■","■"]]
def print_pboard(pboard):
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
            s+=str(test_board[j][i])
            s+=" "
        print(s)

# print_pboard(test_board)

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

# test_board_2 = [[1,1,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]]
# for i in range(len(test_board_2)):
#     print(test_board_2[i])
# summed_board=sum_mines(test_board_2)
# for i in range(len(test_board_2)):
#     print(summed_board[i])
