#!/bin/python3

import math
import os
import random
import re
import sys

'''
You are given a square grid with some cells open (.) and some blocked (X). Your
playing piece can move along any row or column until it reaches the edge of the
grid or a blocked cell. Given a grid, a start and a goal, determine the minmum
number of moves to get to the goal.
'''


#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

import sys
import heapq

class Node:
    def __init__(self, grid_x:int, grid_y:int, impassable:bool) -> None:
        self.set_x(grid_x)
        self.set_y(grid_y)
        self.set_g_cost(sys.maxsize)
        self.set_f_cost(sys.maxsize)
        self.set_h_cost(0)
        self.set_impassable(impassable)
        self.__parent=None
    
    def __lt__(self, other:'Node'):
        return self.get_f_cost() < other.get_f_cost()

    def set_x(self,grid_x:int):
        self.__x=grid_x

    def set_y(self,grid_y:int):
        self.__y=grid_y

    def set_f_cost(self,f_cost:int):
        self.__f_cost=f_cost

    def set_g_cost(self,g_cost:int):
        self.__g_cost=g_cost

    def set_h_cost(self,h_cost:int):
        self.__h_cost=h_cost

    def set_impassable(self,impass:bool):
        self.__impassable=impass

    def set_parent(self,parent_node:'Node'):
        self.__parent=parent_node

    def get_x(self)->int:
        return self.__x
    
    def get_y(self)->int:
        return self.__y
        
    def get_g_cost(self)->int:
        return self.__g_cost
    
    def get_f_cost(self)->int:
        return self.__f_cost

    def get_h_cost(self)->int:
        return self.__h_cost
    
    def get_impassable(self)->bool:
        return self.__impassable

    def get_parent(self)->'Node':
        return self.__parent

class Grid:
    def __init__(self, grid_arr:list[list[str]],start_row:int,start_col:int,goal_row:int,goal_col:int) -> None:
        self.grid_nodes_arr=[]
        self.start_row=start_row
        self.start_col=start_col
        self.goal_row=goal_row
        self.goal_col=goal_col
        self.grid_row_size=len(grid_arr[0])
        self.grid_col_size=len(grid_arr)

        for row in range(self.grid_col_size):
            temp=[]
            for col in range(self.grid_row_size):
                temp.append(self.grid_string_to_node(grid_arr[row][col],row,col))
            self.grid_nodes_arr.append(temp)

        self.get_start().set_g_cost(0)
        self.get_start().set_f_cost(0)

    def grid_string_to_node(self, grid_string:str, row:int, col:int)->Node:
        impassable=False
        if(grid_string=='X'):
            impassable=True
        return Node(row,col,impassable)

    def get_grid_nodes_arr(self, row:int,col:int)->Node:
        return self.grid_nodes_arr[row][col]

    def get_start(self)->Node:
        return self.get_grid_nodes_arr(self.start_row,self.start_col)
    
    def get_goal(self)->Node:
        return self.get_grid_nodes_arr(self.goal_row,self.goal_col)

    def get_x_size(self)->int:
        return self.grid_row_size
    
    def get_y_size(self)->int:
        return self.grid_col_size

def a_star(grid)->list[Node]:
    open_list=[]
    closed_list=[]
    start:Node=grid.get_start()
    goal:Node=grid.get_goal()

    heapq.heappush(open_list,start)

    while open_list:
        current_node:Node=heapq.heappop(open_list)

        if current_node == goal:
            path=[]
            while current_node.get_parent():
                path.append(current_node)
                current_node=current_node.get_parent()
            path.append(current_node)
            return(path[::-1])
        
        closed_list.append(current_node)

        for neighbour in get_neighbours(current_node,grid):
            if neighbour in closed_list or neighbour.get_impassable():
                continue

            g_cost = current_node.get_g_cost() + get_distance(current_node,neighbour)
            if(g_cost<neighbour.get_g_cost()):
                neighbour.set_parent(current_node)
                neighbour.set_g_cost(g_cost)
                neighbour.set_h_cost(get_distance(neighbour,goal))
                neighbour.set_f_cost(neighbour.get_g_cost()+neighbour.get_h_cost())

                if(neighbour not in open_list):
                    heapq.heappush(open_list,neighbour)

    return None

def get_neighbours(node:Node,grid:Grid)->list[Node]:
    neighbours=[]
    values=[-1,0,1]
    for dx in values:
        for dy in values:
            if dx == 0 and dy == 0:
                continue
            x = node.get_x() + dx
            y = node.get_y() + dy
            if (abs(dx)==abs(dy)):
                # horizontal and vertical movement only.
                continue
            if(x<0 or x>=grid.get_x_size() or y<0 or y>=grid.get_y_size()):
                continue
            neighbours.append(grid.get_grid_nodes_arr(x,y))
    return neighbours

def get_distance(node1:Node,node2:Node)->int:
    if node1.get_x() == node2.get_x() or node1.get_y() == node2.get_y():
        # Nodes are in the same row or column
        return 1
    else:
        # Nodes are not in the same row or column
        return (abs(node1.get_x()-node2.get_x())+abs(node1.get_y()-node2.get_y()))

def calculate_straight_lines_of_movement(path:list[Node])->int:
    count=0
    current_direction=None
    x,y=path[0].get_x(),path[0].get_y()
    for p in path[1:]:
        x_temp,y_temp=p.get_x(),p.get_y()
        if(current_direction):
            if(current_direction=='x'):
                if(x!=x_temp):
                    current_direction='y'
                    count+=1
            else:
                if(y!=y_temp):
                    current_direction='x'
                    count+=1
        else:
            if(x==x_temp):
                current_direction='x'
            else:
                current_direction='y'
            count+=1
        x,y=x_temp,y_temp
    return count

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    # coordinates are not cartesian
    start_row,start_col=startX,startY
    goal_row,goal_col=goalX,goalY
    node_grid_arr=Grid(grid,start_row,start_col,goal_row,goal_col)
    path=a_star(node_grid_arr)

    for p in path:
        print(p.get_x(), p.get_y())
    return(calculate_straight_lines_of_movement(path))


if __name__ == '__main__':

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
