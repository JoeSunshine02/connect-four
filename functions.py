def row_checker(direction, distance, peice):
    this_direction = direction
    this_distance = distance
    this_peice=peice

    #print("i am in the row selector")
    match this_direction:
        case 0:
            #right up
            #print("i am in the row selector 0")
            return this_peice[1]+this_distance
        case 1:
            #right
            #print("i am in the row selector 1")
            return this_peice[1]+this_distance
        case 2:
            #right down
            #print("i am in the row selector 2")
            return this_peice[1]+this_distance
        case 3:
            #down
            #print("i am in the row selector 3")
            return this_peice[1]
        case 4:
            #left down
            #print("i am in the row selector 4")
            return this_peice[1]-this_distance
        case 5:
            #left
            #print("i am in the row selector 5")
            return this_peice[1]-this_distance
        case 6:
            #left up
            #print("i am in the row selector 6")
            return this_peice[1]-this_distance
        
    #return the board position at the top left, at x places out
    return -1

def col_checker(direction, distance, peice):
    this_direction = direction
    this_distance=distance
    this_peice = peice
    #print("i am in the col selector")
    match this_direction:
        case 0:
            #rigth up
            #print("i am in the col selector 0")
            print(peice[0])
            return this_peice[0]-this_distance
        case 1:
            #right
            #print("i am in the col selector 1")
            return this_peice[0]
        case 2:
            #right down
            #print("i am in the col selector 2") 
            return this_peice[0]+this_distance
        case 3:
            #down
            #print("i am in the col selector 3")
            return this_peice[0]+this_distance
        case 4:
            #left down
            #print("i am in the col selector 4")
            return this_peice[0]+this_distance
        case 5:
            #left
            #print("i am in the col selector 5")
            return this_peice[0]
        case 6:
            #left up
            #print("i am in the col selector 6")
            return this_peice[0]-this_distance
        
    return -1

def win_check(last_placed_peice, board, player):

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