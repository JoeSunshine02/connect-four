from array import *
from functions import col_checker, row_checker

#empty board to load for game. 
#saved seperate for repeate games
saved_board =[['x','x','x','x','x','x','x','x','x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x',0,0,0,0,0,0,0,'x'],
        ['x','x','x','x','x','x','x','x','x']]

#reserve empty board, used for testing.
reserve_board =[['x','x','x','x','x','x','x','x','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],
        ['x','_','_','_','_','_','_','_','x'],        
        ['x','x','x','x','x','x','x','x','x']]

#win check function, needs to be called after every move.
def win_check(last_placed_peice):

    #checks the eight cardinal directions for a win.
    for direction in range(7):
        win =0
        #checks for four matching peices in a row.
        #win = win + board[last_placed_peice[0]][last_placed_peice[1]]
        #print(win)
        for distance in range(4):
            col=col_checker(direction, distance, last_placed_peice)
            row=row_checker(direction, distance, last_placed_peice)
            #check the value of the peice in the direction that is being checked.
            peice = board[col][row]

            #check for board boarders. (this should probobly be a try catch statment, but im not going to rework the code)
            if peice is 'x':
                break
            win = win + peice
           

        if win/4 == player:
           return 1
    return 0

#get board from saved board
board = saved_board

#set player
player =-1

#set default placed location
#(find out if this is required for function)
last_placed= [0,0]

#set 20 turn limit, change to while loop when win function works
for x in range(20):

    #print play, and board
    print("player is")
    print(player)
    for x in board:
        print(x)

    #set and check input, repeate inputs until vlaid input is entered
    #set check vars inside valid range
    input_check=False
    input_col=1
    row_selector=6

    while input_check == False:
        input_col=int(input("pick a row between 1 and 7"))
        if input_col >=1 and input_col<=7:
            input_check = True

    #place peice at the lowest possible location in column
    while row_selector>0:
        if board[row_selector][input_col] != 0:
            row_selector = row_selector -1
        else:
            board[row_selector][input_col]=player
            last_placed=[row_selector,input_col]
            break

    #determin if game ties.
    #this will need to change, best option is to disable button in app
    if row_selector==0:
        #return game is a tie!
        print("game is a tie")
        break


    #print the location of the last placed peice
    #print(last_placed)
    win_check(last_placed, player, board)
    
    

    #function call for 
    #if win_check(base_col, base_row,4) ==1:
    #    break


   

    #swap player turn id
    if player == -1:
        player = 1
    else:
        player = -1