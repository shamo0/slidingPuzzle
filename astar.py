from Board import *
from Board import manhattanDistance
from Board import misplacedTiles

class aStar(board=Board.b, heuristics=None):

    search = {
        'manhattanDistance': manhattanDistance,
        'misplacedTiles' : misplacedTiles,
    }   

    heuristic  = search[str(heuristics)]


    def __init__(self, parent=None, position=None):
        self.position = position
        self.parent = parent

        self.g = 0
        self.h = 0 
        self.f = 0

    def algorithm(self,start,end):
        number_expanded = 0

        #Start Node
        start_node = aStar(None,start)
        start_node.g = 0
        start_node.h = 0
        start_node.f = 0

        #End Node
        end_node = aStar(None,end)
        end_node.g = 0
        end_node.h = 0
        end_node.f = 0
        
        #Initializing Open and Closed Lists
        open_list = []
        closed_list = []

        while open_list:

            current_node = open_list[0]
            current_node_index = 0
            

            for index, item in enumerate(open_list):
                current_node = item
                current_node_index = index
            
            #We pop from Open and append to Closed
            open_list.pop(current_node_index)
            closed_list.append(current_node)
            
            #The goal is found
            if current_node == end_node:
                path = []
                current = current_node
                while current:
                    path.append(current.position)
                    current = current.parent
                
                return path[::-1], number_expanded

            children = Board.generateMoves()

            for child in children:
                
                for i in closed_list:
                    if child == i:
                        continue
                
                child.g = current_node.g + 1
                child.h = heuristic(child.position,end_node.position)
                child.f = child.g + child.h
                
                for node in open_list:
                    if (child == node) and (child.g > node.g):
                        continue
                
                open_list.append(child)

            number_expanded += 1 

        return path[::-1], number_expanded


ors(s)
#         for i in successors:
#             successor_cost = f_Cost(i)
#             successor_parent = s
#         if s not in closed:
#             CLOSED.append(s)
#             OPEN.put(s)

#     return OPEN.get()

if __name__ == "__main__":

    astar()
    # CLOSED = []
    # OPEN = PriorityQueue()

    # s = startState
    
    # astar()


