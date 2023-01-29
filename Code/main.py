
from random import random
from time import time
mode=input("Choose mode: (e=easy, m=medium, h=hard): ")
E_SIZE=10
M_SIZE=20
H_SIZE=50
C_SIZE=0
M_DENS=0.15

#set C_SIZE (chosen size)
match mode:
    case "e":
        C_SIZE=E_SIZE
    case "m":
        C_SIZE=M_SIZE
    case "h":
        C_SIZE=H_SIZE

#Initialize boards, "game" and "player" boards
g_board = [[(1 if random()<M_DENS else 0) for j in range(C_SIZE)] for i in range(C_SIZE)]
p_board = [[0 for j in range(C_SIZE)] for i in range(C_SIZE)]
# for i in range(C_SIZE):
#     print(board[i])

#Timer
iTime=time()

#states
state=0
while state==0:
    x=input("")
