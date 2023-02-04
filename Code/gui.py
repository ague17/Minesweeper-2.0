import tkinter as tk

tablero = []
def which_button(button_press):
    x, y = button_press
    tablero[x][y].configure(bg="red", fg="yellow")

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

button = tk.Button(root, text="Start Game", font=('Arial',12))
button.pack(pady=5)

#frames (like areas to place stuff)
mainFrame = tk.Frame()
mainFrame.pack(expand=1) #Configurar el metodo pack()
# mainFrame.config(bg="blue")
mainFrame.config(width="150", height="150")

#place thing in frame:
C_SIZE_R = 15
C_SIZE_C = 10
for i in range(C_SIZE_R):
    fila_tablero = []
    for j in range(C_SIZE_C):
        button = tk.Button(mainFrame, text=" ", font=("Arial",10), \
        command=lambda m=[i,j]: which_button(m))
        fila_tablero.append(button)
        button.grid(row=j, column=i)
    tablero.append(fila_tablero)
#run root
root.mainloop()
