from random import random
from time import time
import numpy as np
from utils import *
import tkinter as tk

E_SIZE=10
M_SIZE=20
H_SIZE=50
C_SIZE=0
M_DENS=0.08
M_DENS_TOL=0.02


tablero = []
exploradas = 0
num_mines = 0
s_board = []
p_board = []
def which_button(button_press):
    global exploradas
    global root
    global s_board
    global p_board
    global tablero
    x, y = button_press
    exploradas+=explore(x, y, s_board, p_board, tablero)
    if exploradas+num_mines>=C_SIZE*C_SIZE:
        print("Ganado supuestamente")
        root.destroy()
    if s_board[x][y]=="X":
        print("Perdido supuestamente")
        root.destroy()

def choose_dif(mode, frame):
    #set C_SIZE (chosen size)
    global C_SIZE
    global C_SIZE
    global C_SIZE
    global C_SIZE
    if mode=="e": C_SIZE=E_SIZE
    elif mode=="m": C_SIZE=M_SIZE
    elif mode=="h": C_SIZE=H_SIZE
    else:
        print("Invalid mode chosen. Quitting")
        quit()
    frame.destroy()
    game_start()


def game_start():

    global C_SIZE
    global num_mines
    global p_board
    global s_board

    while num_mines>(M_DENS+M_DENS_TOL)*C_SIZE*C_SIZE or num_mines<(M_DENS-M_DENS_TOL)*C_SIZE*C_SIZE:
        g_board = [[(1 if random()<M_DENS else 0) for j in range(C_SIZE)] for i in range(C_SIZE)]
        #count mines
        num_mines=np.sum(g_board)
        print("Number of mines: ", num_mines)

    p_board = [["■" for j in range(C_SIZE)] for i in range(C_SIZE)]
    s_board = sum_mines(g_board)

    #frames (like areas to place stuff)
    mainFrame = tk.Frame()
    mainFrame.pack(expand=1) #Configurar el metodo pack()
    # mainFrame.config(bg="blue")
    mainFrame.config(width="150", height="150")

    #place thing in frame:
    for i in range(C_SIZE):
        fila_tablero = []
        for j in range(C_SIZE):
            button = tk.Button(mainFrame, text="  ", font=("Arial",10), \
            command=lambda m=[i,j]: which_button(m))
            fila_tablero.append(button)
            button.grid(row=j, column=i)
        tablero.append(fila_tablero)
    #run root

    print("Después de main loop")
    # for i in range(C_SIZE):
    #     print(board[i])

    #Timer
    iTime=time()

#Initialize boards, "game" and "player" boards
print("csize is", str(C_SIZE))

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
dif_frame = tk.Frame()
dif_frame.pack(expand=1)
dif_frame.config(width="100", height="20")

#easy button
button_e = tk.Button(dif_frame, text="EASY", font=("Arial",10), \
command=lambda m="e": choose_dif(m, dif_frame))
button_e.grid(column=0, row=0, padx=(10,10))
#medium button
button_m = tk.Button(dif_frame, text="MEDIUM", font=("Arial",10), \
command=lambda m="m": choose_dif(m, dif_frame))
button_m.grid(column=1, row=0, padx=(10,10))
#hard button
button_h = tk.Button(dif_frame, text="HARD", font=("Arial",10), \
command=lambda m="h": choose_dif(m, dif_frame))
button_h.grid(column=2, row=0, padx=(10,10))

root.mainloop()

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
