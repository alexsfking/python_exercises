#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
# Given a square grid of characters in the range ascii[a-z], 
# rearrange elements of each row alphabetically, ascending. 
# Determine if the columns are also in ascending alphabetical 
# order, top to bottom. Return YES if they are or NO if they 
# are not.
#


def gridChallenge(grid):
    # Write your code here
    new_grid=[]
    for row in grid:
        temp=list(row)
        temp.sort()
        new_grid.append("".join(temp))
    for row in new_grid:
        print(row)
    new_grid=list(map(list,zip(*new_grid)))
    for row in new_grid:
        temp=row
        temp.sort()
        for i in range(len(temp)):
            if(temp[i]!=row[i]):
                print(temp, row)
                return "NO"
    return "YES"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
