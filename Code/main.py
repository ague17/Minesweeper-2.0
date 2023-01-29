
from random import random
from time import time
import numpy as np
mode=input("Choose mode: (e=easy, m=medium, h=hard): ")
E_SIZE=10
M_SIZE=20
H_SIZE=50
C_SIZE=0
M_DENS=0.15
M_DENS_TOL=0.02

#set C_SIZE (chosen size)
match mode:
    case "e":
        C_SIZE=E_SIZE
    case "m":
        C_SIZE=M_SIZE
    case "h":
        C_SIZE=H_SIZE

#Initialize boards, "game" and "player" boards
num_mines=0
while num_mines>(M_DENS+M_DENS_TOL)*C_SIZE*C_SIZE or num_mines<(M_DENS-M_DENS_TOL)*C_SIZE*C_SIZE:
    g_board = [[(1 if random()<M_DENS else 0) for j in range(C_SIZE)] for i in range(C_SIZE)]
    #count mines
    num_mines=np.sum(g_board)
    print("Number of mines: ", num_mines)


p_board = [["■" for j in range(C_SIZE)] for i in range(C_SIZE)]



# for i in range(C_SIZE):
#     print(board[i])

#Timer
iTime=time()

#states
discovered_cells=0
state=0
while state==0:
    chosen_cell=input("Enter the cell you want to discover (example: A3): ")
    #tendríamos que protegerlo, dentro del rango de C_SIZE
    x=ord(chosen_cell[0])-65
    y=int(chosen_cell[1])-1

    #perder
    if g_board[x][y]==1:
        state=-1
        break
    #ganar
    if g_board[x][y]==0:
        pass
        #if discovered_cells==C_SIZE*C_SIZE-
    break
