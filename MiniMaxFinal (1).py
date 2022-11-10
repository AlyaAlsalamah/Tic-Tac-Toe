# Tic Tac Toe game with MiniMax algorithm
#




from asyncio.windows_events import INFINITE
import timeit
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time

end = 0
start = 0
playerTurn = True

depth = 9
end_depth = size =  total =0
tree_depth = -1

player = 'X'
computer = 'O'


assigned_places =[]

root = Tk()
root.title("Tic Tac Toe")
# add Buttons
button1 = ttk.Button(root, text=' ')
button1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
button1.config(command=lambda: ButtonClick(1))


button2 = ttk.Button(root, text=' ')
button2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
button2.config(command=lambda: ButtonClick(2))


button3 = ttk.Button(root, text=' ')
button3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
button3.config(command=lambda: ButtonClick(3))


button4 = ttk.Button(root, text=' ')
button4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
button4.config(command=lambda: ButtonClick(4))


button5 = ttk.Button(root, text=' ')
button5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
button5.config(command=lambda: ButtonClick(5))

button6 = ttk.Button(root, text=' ')
button6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
button6.config(command=lambda: ButtonClick(6))

button7 = ttk.Button(root, text=' ')
button7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
button7.config(command=lambda: ButtonClick(7))

button8 = ttk.Button(root, text=' ')
button8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
button8.config(command=lambda: ButtonClick(8))

button9 = ttk.Button(root, text=' ')
button9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
button9.config(command=lambda: ButtonClick(9))

playerdetails = ttk.Label(root, text=" X is you \n O is the computer")
playerdetails.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)
style = ttk.Style()
style.configure("BW.TLabel", background="black", foreground="white")
res = ttk.Button(root, text='Restart')
res.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
res.config(command=lambda: reset())


buttons = [None, button1, button2, button3, button4,
           button5, button6, button7, button8, button9]


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def reset():
    global depth, end_depth,total, size, tree_depth, playerTurn,assigned_places,start,end     
    depth = 9
    tree_depth = -1
    end_depth = size = 0
    playerTurn = True
    assigned_places=[]
    start=end=total=0

    resetButtons()


def resetButtons():
    global board
    for i in range(1, len(buttons)):
        buttons[i]['text'] = ' '
        buttons[i].state(['!disabled'])

    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}


def desiableButtons():
    for i in range(1, len(buttons)):
        buttons[i].state(['disabled'])

# Method that takes a letter which indicates who's the current player, and a position to place the letter on.
def assign(letter, position):
    global tree_depth
    if board[position] == ' ':
        tree_depth += 1

        board[position] = letter
        buttons[position]['text'] = letter

        assigned_places.append(position)

        if isdraw():
            desiableButtons()
            tkinter.messagebox.showinfo("Tic Tac Toe", ("Winner is draw", (f"The ending depth is : {end_depth}"), (
                f"The depth of tree : {tree_depth}"), (f"The size is : {size} "),(f"The size is : {size} "),(f"the time tooken : {(total)}")))

        if is_win(player):
            desiableButtons()
            tkinter.messagebox.showinfo("Tic Tac Toe", ("Winner is player", (f"The ending depth is : {end_depth}"), (
                f"The depth of tree : {tree_depth}"), (f"The size is : {size} "),(f"the time tooken : {(total)}")))

        elif is_win(computer):
            desiableButtons()
            tkinter.messagebox.showinfo("Tic Tac Toe", ("Winner is computer", (f"The ending depth is : {end_depth}"), (
                f"The depth of tree : {tree_depth}"), (f"The size is : {size} "),(f"the time tooken : {(total)}")))

        return

    return


def ButtonClick(id):
    global start,end,total
    if playerTurn and id not in assigned_places:
        Human(id)
        start = timeit.default_timer()
        Computer()
        end = timeit.default_timer()
        total+= end-start 

# Human moves happens here and sending the move to the assign method to assign the move.
def Human(position):
    global playerTurn
    playerTurn = False
    assign(player, position)

    return

#Computer move that will be sent to the "AI" algorithm to decide if the move is efficient.
def Computer():
    MaxScore = -INFINITE
    Move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer

            score = min_value(board,depth-1) # Sending values to MiniMax 
            board[key] = ' '

            if score > MaxScore:
                MaxScore = score
                Move = key

    global playerTurn
    assign(computer, Move)
    playerTurn = True

    return


def terminal():
            global size
            size = size+1
            return possible_win(computer) or possible_win(player) or isdraw()

def isdraw():
    return " " not in board.values()

def is_win(symbol):
    if ((button1['text'] == button2['text'] and button2['text'] == button3['text'] and button1['text'] == symbol) or
        (button4['text'] == button5['text'] and button5['text'] == button6['text'] and button4['text'] == symbol) or
        (button7['text'] == button8['text'] and button8['text'] == button9['text'] and button7['text'] == symbol) or
        (button1['text'] == button4['text'] and button4['text'] == button7['text'] and button1['text'] == symbol) or
        (button2['text'] == button5['text'] and button5['text'] == button8['text'] and button2['text'] == symbol) or
        (button3['text'] == button6['text'] and button6['text'] == button9['text'] and button3['text'] == symbol) or
        (button1['text'] == button5['text'] and button5['text'] == button9['text'] and button1['text'] == symbol) or
        (button3['text'] ==     button5['text'] and button5['text'] == button7['text'] and button3['text'] == symbol)):
        return True
    else:
        return False


def possible_win(symbol):

    return (board[1] == board[2] and board[1] == board[3] and board[1] == symbol or
            board[4] == board[5] and board[4] == board[6] and board[4] == symbol or
            board[7] == board[8] and board[7] == board[9] and board[7] == symbol or
            board[1] == board[4] and board[1] == board[7] and board[1] == symbol or
            board[2] == board[5] and board[2] == board[8] and board[2] == symbol or
            board[3] == board[6] and board[3] == board[9] and board[3] == symbol or
            board[1] == board[5] and board[1] == board[9] and board[1] == symbol or
            board[7] == board[5] and board[7] == board[3] and board[7] == symbol)


def utility():
    if possible_win(computer):
        return 10-depth
    elif possible_win(player):
        return depth-10
    elif isdraw():
        return 0


def max_value(board, depth):
    global end_depth
    if terminal():
        end_depth = depth
        return utility()

    MaxScore = -INFINITE

    for key in board.keys():

        if board[key] == ' ':
            board[key] = computer

            score = min_value(board, depth-1)
            board[key] = ' '  # undo

            MaxScore = max(MaxScore, score)


    return MaxScore


def min_value(board,depth):
    global end_depth

    if terminal():        
        end_depth = depth
        return utility()

    MinScore = INFINITE

    for key in board.keys():

        if board[key] == ' ':
            board[key] = player
            score = max_value(board,depth-1)
            board[key] = ' '

            MinScore = min(MinScore, score)

    return MinScore


root.mainloop()
