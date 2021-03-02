# 15 Sliding Puzzle

4x4 15 piece sliding puzzle solution using A* and IDA* algorithms (Python implementation)

![puzzle](15puzzle.svg.png)

## Problem

The 15-Puzzle is the obvious extension of the 8-Puzzle to a 4 by 4 grid. Program solves the 15-puzzle using A* and IDA*. 

## A*

A* Function takes baord and heuristic function as argument and returns a tuple of moves to solve it and the number of nodes expanded , as in: [[2,2],[1,2],[0,2],[0,1],[0,0]]. and 154.

## IDA*

IDA* Function takes board and heuristic function as argument and returns a tuple of moves to solve it and the number of nodes expanded (same as A*).

## Heuristics

For the problem we are using Manhattan Distance and misplaced tiles heuristics. 
