from aStar import *
from idaStar import *
from Board import *
# from PriQue import *
import copy
import pdb

search = {
    'aStar': aStar,
    'idaStar' : idaStar,
}


if __name__ == "__main__":
    n = int(input("Enter scramble size: ")) 
    funStr = input("Enter search function: ")
    f = search[funStr]

    # b1 = Board()
    # b1.scramble(n)
    # b2 = Board()

    # p , n1  = f(b1, misplacedTiles)
    # print(len(p))
    # applyMoves(b1,p)
    # print(b1==b2)

    b1 = Board()
    b1.scramble(n)
    p , n2  = f(b1, manhattanDistance)
    print(len(p))
    print(f(b1, manhattanDistance))
    # applyMoves(b1,p)
    # print(b1==b2)
    # print(n1>=n2)