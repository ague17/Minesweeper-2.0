import tkinter as tk

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
C_SIZE_R=10
C_SIZE_C=15
for i in range(C_SIZE_R):
    for j in range(C_SIZE_C):
        button = tk.Button(mainFrame, text="X", font=("Arial",10))
        button.grid(row=i, column=j)

#run root
root.mainloop()
