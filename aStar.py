from queue import PriorityQueue
from Board import *
from Board import manhattanDistance
from Board import misplacedTiles
import copy

def aStar(board, heuristics):

    path = []
    number_expanded = 0
    goal = [['b', 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    print(str(board.b))

    current_board = board
    
    # #Defining CLOSED and OPEN
    open_list = []
    closed_list = []

    open_list.append(current_board)

    while len(open_list)>0:
        

        current_board = open_list[0]
        current_board_index = 0

        for index, item in enumerate(open_list):
            if current_board.f > item.f:
                current_board = item
                current_board_index = index

        open_list.pop(current_board_index)
        closed_list.append(current_board)


        #Check if we are at the goal state
        if board.__eq__(goal):
            # print(board.b)
            # print('\n')
            print("Found Goal")
            current = current_board

            while True: #while not root
                path.append(current.lb)
                try:
                    current = current.parent
                except:
                    return path[::-1], number_expanded
                        
            # Return path and number of expanded nodes
            

        #Generating Children Nodes
        children = board.generateMoves()
        print("Printing Children Nodes")
        print(children)
        print('\n')

        #Iterating thru the children nodes
        for move in children:
            print("Printing Individual Moves and new states")
            # print(move)
            
            #making copies of the board before making the moves
            new_state = copy.deepcopy(board)
            new_state.parent = board.lb

            new_state.makeMove(move)
            print(new_state.b)

            #If already seen the child or child with worse score
            # if (new_state.b in closed_list) and (new_state.g < current_board.g):
            #     break
            
        
            #Heuristic. f(n) = g(n) + h(n)
            new_state.g = current_board.g + 1
            new_state.h = heuristics(new_state.b)
            new_state.f = new_state.g + new_state.h

            # Testing 
            print("G cost: ", new_state.g)
            print("H cost: ", new_state.h)
            print("F cost: ", new_state.f)
            print('\n')


            open_list.append(new_state)

            if new_state not in closed_list:
                closed_list.append(new_state)

            
        number_expanded += 1 


    
