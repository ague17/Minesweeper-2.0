from random import random
from time import time
import numpy as np
from utils import *
import tkinter as tk

tablero = []
def which_button(button_press):
    x, y = button_press
    explore(x, y, s_board, p_board, tablero)

mode=input("Choose mode: (e=easy, m=medium, h=hard): ")
E_SIZE=10
M_SIZE=20
H_SIZE=50
C_SIZE=0
M_DENS=0.08
M_DENS_TOL=0.02

#set C_SIZE (chosen size)
if mode=="e": C_SIZE=E_SIZE
elif mode=="m": C_SIZE=M_SIZE
elif mode=="h": C_SIZE=H_SIZE
else:
    print("Invalid mode chosen. Quitting")
    quit()

#Initialize boards, "game" and "player" boards
num_mines=0
while num_mines>(M_DENS+M_DENS_TOL)*C_SIZE*C_SIZE or num_mines<(M_DENS-M_DENS_TOL)*C_SIZE*C_SIZE:
    g_board = [[(1 if random()<M_DENS else 0) for j in range(C_SIZE)] for i in range(C_SIZE)]
    #count mines
    num_mines=np.sum(g_board)
    print("Number of mines: ", num_mines)

p_board = [["■" for j in range(C_SIZE)] for i in range(C_SIZE)]
s_board = sum_mines(g_board)

#init app after setting difficulty (TB changed)
#conventional window name
root = tk.Tk()
#window title
root.title("MINESWEEPER 2.0")
#set geometry
root.geometry("500x500")

#adding elements to the root
label = tk.Label(root, text="MINESWEEPER 2.0", font=('Arial',18))
label.pack(padx=0,pady=10)
label = tk.Label(root, text="Developed by\nague17 & Nerocraft4 ",\
                 font=('Arial',8))
label.pack()

#frames (like areas to place stuff)
mainFrame = tk.Frame()
mainFrame.pack(expand=1) #Configurar el metodo pack()
# mainFrame.config(bg="blue")
mainFrame.config(width="150", height="150")

#place thing in frame:
C_SIZE = 10
for i in range(C_SIZE):
    fila_tablero = []
    for j in range(C_SIZE):
        button = tk.Button(mainFrame, text="  ", font=("Arial",10), \
        command=lambda m=[i,j]: which_button(m))
        fila_tablero.append(button)
        button.grid(row=j, column=i)
    tablero.append(fila_tablero)
#run root
root.mainloop()

# for i in range(C_SIZE):
#     print(board[i])

#Timer
iTime=time()
'''
#states
discovered_cells=0
state=0

print_pboard(p_board, False)
print("Enter the cell you want to discover (example: A3). Type a '#' before it \
to flag that cell.")
while state==0:
    chosen_cell=input("Select cell: ")
    #tendríamos que protegerlo, dentro del rango de C_SIZE
    if chosen_cell[0]=="#":
        chosen_cell=chosen_cell[1:]
        x, y = cell2coords(chosen_cell)
        if p_board[x][y]!="■":
            continue
        p_board[x][y]="#"
        print_pboard(p_board, False)
        continue
    x, y = cell2coords(chosen_cell)
    #perder
    if g_board[x][y]==1:
        state=-1
        print("HAS PERDIDO!!!")
        break
    #efecto de descubrir
    new_cells_discovered = explore(x, y, s_board, p_board)
    discovered_cells = discovered_cells + new_cells_discovered
    print_pboard(p_board, False)
    print("Cells to discover ", C_SIZE*C_SIZE-num_mines-discovered_cells)
    #ganar
    if discovered_cells==C_SIZE*C_SIZE-num_mines:
        print("HAS GANADO!!!")
        #if discovered_cells==C_SIZE*C_SIZE-
        break
'''
