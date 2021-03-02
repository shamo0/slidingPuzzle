from queue import PriorityQueue
from Board import *
from Board import manhattanDistance
from Board import misplacedTiles
import copy

def aStar(board, heuristics):

    path = []
    number_expanded = 0
    goal = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    # #Defining CLOSED and OPEN
    OPEN = []
    CLOSED = dict()

    OPEN.append(board)

    while len(OPEN)>0:

        board = OPEN[0]
        board_index = 0
        for index, item in enumerate(OPEN):
            if item.key() in CLOSED:
                continue
            elif board.f > item.f:
                board = item
                board_index = index

        CLOSED[board.key()] = board.f
        OPEN.pop(board_index)
        number_expanded += 1
        
        #Check if we are at the goal state
        if board.__eq__(goal):
                current = board
                path.append(current.lb)
                while current.parent is not None:
                    path.append(current.parent.lb)
                    current = current.parent
                return list(reversed(path[:-1])), number_expanded
                                
        #Generating Children Nodes
        children = board.generateMoves()

        #Iterating thru the children nodes
        for move in children:            
            #making copies of the board before making the moves
            new_state = copy.deepcopy(board)
            new_state.parent = board

            new_state.makeMove(move)

            new_state.g = board.g + 1
            new_state.h = heuristics(new_state.b)
            new_state.f = new_state.g + new_state.h 

            if new_state.key() in CLOSED:
                if new_state.f < CLOSED[new_state.key()]:
                    CLOSED[new_state.key()] = new_state.f
                else:
                    continue

            if new_state not in OPEN:
                OPEN.append(new_state)

        


    
