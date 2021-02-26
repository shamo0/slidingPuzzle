from queue import PriorityQueue
from Board import *
from Board import manhattanDistance
from Board import misplacedTiles
import copy

def idaStar(board, heuristics):
    limit = 0
    done == False
    number_expanded = 0
    goal = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    print(str(board.b))

    current_board = board
    
    # #Defining CLOSED and OPEN
    open_list = []
    closed_list = []
    path = []



    while not done:
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
            
            
            
    