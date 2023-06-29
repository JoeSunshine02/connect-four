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

board = saved_board
player =-1
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
        if board[row_selector][input_col] != 0:
            row_selector = row_selector -1
        else:
            board[row_selector][input_col]=player
            break

    if row_selector==0:
        #return game is a tie!
        print("game is a tie")
        break

    if player == -1:
        player = 1
    else:
        player = -1