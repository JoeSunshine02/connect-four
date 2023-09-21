from flask import Flask, render_template, request, redirect
from array import *
from functions import *
saved_board =[['x','x','x','x','x','x','x','x','x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x','x','x','x','x','x','x','x','x']]

board = saved_board
player =1
last_placed_peice=[0,0]
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('landing_page.html')
    

@app.route('/game_board')
def game_board():
    return render_template('game_page.html', board = board, player = player)


@app.post('/place_peice')
def place_peice():
    row_selector=6
    global player
    global last_placed_peice

    input_col = int(request.form.get('row'))

    while row_selector>0:
        if board[row_selector][input_col] != 0:
            row_selector = row_selector -1
        else:
            board[row_selector][input_col]=player
            last_placed_peice =[row_selector,input_col]
            break

    return redirect("/check_win")

@app.get('/check_win')
def check_peice():
    global player
    global last_placed_peice
    if win_check(last_placed_peice,board,player)==1:
        return redirect("/game_win")

    if player == 1:
        player = -1
    else:
        player = 1
    return redirect("/game_board")

@app.route('/game_win')
def game_win():
    global player
    return render_template('end_page.html', player = player)