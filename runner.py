
import minmax as mm
import tkinter as tk
from tkinter import messagebox

board = [[0, 0, 0] for _ in range(3)]
current_player = 1


def main():
    global current_player
    global user
    buttons = [['', '', ''] for _ in range(3)]
    root = tk.Tk()
    root.title("Tic Tac Toe")

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text="", font=('normal', 30), width=4, height=2,
                                    command=lambda row=i, col=j: click(row, col, buttons,root))
            buttons[i][j].grid(row=i, column=j)
    root.mainloop()

def click(row, col, buttons,root):

    global board
    global user
    global current_player
    obj=mm.board()
    if buttons[row][col]["text"] == "":
        if current_player == 1:
            board[row][col] = 1
            player_symbol = 'X'
            current_player = -1
        else:
            board[row][col] = -1
            player_symbol = 'O'
            current_player = 1
        buttons[row][col]["text"] = player_symbol
        if obj.terminal(board):
            if obj.winner(board) == 1:
                root.destroy()
                box=messagebox.showinfo("Winner",'X win')
            elif obj.winner(board) == -1:
                root.destroy()
                box=messagebox.showinfo("Winner",'O win')
            else:
                root.destroy()
                box=messagebox.showinfo("Tie Game", 'Tie Game')

    temp=''
    new = mm.board()
    move=new.minimax(board)
    i=move[0]
    j=move[1]
    board[i][j]=current_player
    if current_player==1:
        temp='X'
        current_player=-1
    else:
        temp='O'
        current_player=1

    buttons[i][j]["text"]=temp
    if obj.terminal(board):
            if obj.winner(board) == 1:
                root.destroy()
                box=messagebox.showinfo("Winner",'X win')
            elif obj.winner(board) == -1:
                root.destroy()
                box=messagebox.showinfo("Winner",'O win')
            else:
                root.destroy()
                box=messagebox.showinfo("Tie Game", 'Tie Game')


    

main()
