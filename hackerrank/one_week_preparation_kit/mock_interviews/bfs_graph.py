#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

from collections import deque

def bfs(n, m, edges, s):
    # Write your code here
    q=deque()
    d=dict()
    cost=6
    for i in range(1,n+1):
        d[i]=[]
    for e in edges:
        d[e[0]].append(e[1])
        d[e[1]].append(e[0])
        
    visited=dict()
    q.append(s) #root added to queue
    visited[s]=0 #root visited
    while len(q):
        current=q.popleft()
        for e in d[current]:
            if(e not in visited):
                q.append(e)
                visited[e]=visited[current]+1
    #for k,v in visited.items():
        #print(k,v)
    out=[]
    for k in d.keys():
        if(k in visited):
            out.append(visited[k]*cost)
        else:
            out.append(-1)
    out.remove(0)
    return(out)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
