from flask import Flask, render_template, request, redirect
from array import *
saved_board =[['x','x','x','x','x','x','x','x','x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x','x','x','x','x','x','x','x','x']]

reserve_board =[['x','x','x','x','x','x','x','x','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],        
        ['x','x','x','x','x','x','x','x','x']]
board = reserve_board

app = Flask(__name__)

#['x','_','_','_','_','_','_','_','x'],

player ='W'
for x in range(20):

    print(player)
    for x in board:
        print(x)

    input_check=False
    input_col=1
    row_selector=6

    while input_check == False:
        input_col=int(input("pick a row between 1 and 7"))
        if input_col >=1 and input_col<=7:
            input_check = True

    while row_selector>0:
        if board[row_selector][input_col] is not '_':
            row_selector = row_selector -1
        else:
            board[row_selector][input_col]=player
            break

    if row_selector==0:
        #return game is a tie!
        print("game is a tie")
        break

    if player is 'W':
        player = 'o'
    else:
        player = 'W'






@app.route('/')
def index():
    

    return render_template('game_page.html', board = board)