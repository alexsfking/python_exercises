from collections import deque

def get_adjacent(maze:list,visited:set,available:deque,current:tuple):
    row,col=current
    if(col>0 and maze[row][col-1]=='.' and (row,col-1) not in visited ):
        available.append((row,col-1))
    if(col<len(maze[row])-1 and maze[row][col+1]=='.' and (row,col+1) not in visited):
        available.append((row,col+1))
    if(row>0 and maze[row-1][col]=='.' and (row-1,col) not in visited):
        available.append((row-1,col))
    if(row<len(maze[row])-1 and maze[row+1][col]=='.' and (row+1,col) not in visited):
        available.append((row+1,col))
    return available

def path_finder(maze):
    maze=maze.splitlines()
    visited=set()
    start=(0,0)
    available=deque([start])
    goal=(len(maze) - 1,len(maze[len(maze) - 1])-1)
    while(available):
        current=available.pop()
        if(current==goal):
            return True
        visited.add(current)
        available=get_adjacent(maze,visited,available,current)
    return False
