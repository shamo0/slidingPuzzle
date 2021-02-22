from queue import PriorityQueue
from Board import *
from Board import manhattanDistance
from Board import misplacedTiles

class aStar_helper():
    
    def __init__(self, parent=None, position = None):
        self.parent = parent
        self.position = position

        self.g = self.h = self.f = 0

def aStar(board, heuristics):

    print(str(heuristics))
    print(str(board.b))

    print(heuristics(board.b))

    position = None
    parent = None


    number_expanded = 0

    open_list = []
    closed_list = []

    while len(open_list)>0:
        current_node = open_list[0]
        current_node_index = 0

        for index, item in enumerate(open_list):
            current_node = item
            current_node_index = index
        
        open_list.pop(current_node_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current:
                path.append(position)

    
