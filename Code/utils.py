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

print_pboard(test_board)
