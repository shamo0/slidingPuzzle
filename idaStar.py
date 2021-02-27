from queue import PriorityQueue
from Board import *
from Board import manhattanDistance
from Board import misplacedTiles
import copy
import math

def idaStar(board,heuristics):
    current_board = board 
    print("OG board",str(board.b))

    #heuristic
    current_board.g = 0
    current_board.h = heuristics(current_board.b)

    current_board.f = current_board.g + current_board.h
    # l <-- f(s)
    limit = current_board.f
    
    r = 0
    
    while (str(r).isdigit()==True):
        # print("In loop ")
        # current_board.g+=1
        # current_board.h = heuristics(current_board.b)
        # current_board.f = current_board.g + current_board.h
        # # l <-- f(s)
        limit = current_board.f
        # print("Limit: ",limit)
        
        r = F_Limited_DFS(current_board, limit,heuristics)

        if str(r).isdigit():
            # print("r is still length")
            limit = r
    
    return r

def F_Limited_DFS(board, limit,heuristics):

    miniumum = math.inf
    number_expanded = 0

    goal = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    # print(str(board.b))

    current_board = board
    
    # #Defining CLOSED and OPEN
    open_list = []
    closed_list = []
    path = []

    open_list.append(current_board)

    while open_list:

        if current_board.f <= limit:


            #Checking if goal state. If goal return path and # expandend nodes
            if board.__eq__(goal):
                print("Found Goal")
                current = current_board
                while True: #while not root
                    try:
                        parent = current.parent
                        path.append(parent.lb)
                        current = current.parent
                    except:
                        # Return path and number of expanded nodes
                        return path[::-1], number_expanded
            
            children = board.generateMoves()
            print('\n')
            print("Printing Children Nodes")
            print(children)

            for move in children:
                print("Printing Individual Moves and new states")
            
                #making copies of the board before making the moves
                new_state = copy.deepcopy(board)
                new_state.parent = current_board
                print("Parent: ",new_state.parent)

                new_state.makeMove(move)
                print("New State: ", new_state.b)

                new_state.g = current_board.g + 1
                new_state.h = heuristics(new_state.b)
                new_state.f = new_state.g + new_state.h

                open_list.append(new_state)
        
        else:
            print("IN ELSE")
            if current_board.f < miniumum:
                miniumum = current_board.f
        
        
        current_board = open_list.pop()
        board = current_board
        number_expanded += 1
        
    return miniumum
