from queue import PriorityQueue
from Board import *
from Board import manhattanDistance
from Board import misplacedTiles
import copy
import math

def idaStar(board,heuristics):
    #heuristic
    board.g = 0
    board.h = heuristics(board.b)
    board.f = board.g + board.h
    limit = board.f # l <-- f(s)
    
    r = 0
    
    while (str(r).isdigit()==True):
        r = F_Limited_DFS(board, limit, heuristics)
        if str(r).isdigit():
            limit = r    
    return r

def F_Limited_DFS(board, limit,heuristics):
    goal = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    done = False
    miniumum = math.inf
    number_expanded = 0
    # #Defining  OPEN and Path
    open_list = []
    path = []

    open_list.append(board)

    while done == False:
        board.h = heuristics(board.b)
        board.f = board.g + board.h 

        if board.f <= limit:
            #Checking if goal state. If goal return path and # expandend nodes
            if board.__eq__(goal):
                current = board
                path.append(current.lb)
                while current.parent is not None:
                    path.append(current.parent.lb)
                    current = current.parent
                    
                return list(reversed(path[:-1])), number_expanded

            else: 
                children = board.generateMoves()

                for move in children:
                    #making copies of the board before making the moves
                    new_state = copy.deepcopy(board)
                    new_state.parent = board
                    new_state.makeMove(move)
                    new_state.g = board.g + 1
 
                    if new_state not in open_list:
                        open_list.append(new_state)

        else:
            if (board.f < miniumum) or miniumum==None:
                miniumum = board.f
        
        try:
            board = open_list.pop()

        except:
            done = True
        
        
        number_expanded+=1

        
    return miniumum
