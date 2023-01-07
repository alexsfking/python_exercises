#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#

def diagonalDifference(arr):
    # Write your code here
    count_tl_br=0
    count_col=len(arr)-1
    count_bl_tr=0
    
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if(i==j):
                count_tl_br+=arr[i][j]
            if(j==count_col):
                count_bl_tr+=arr[i][j]
                count_col-=1
    return(abs(count_bl_tr-count_tl_br))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
