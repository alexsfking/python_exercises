#!/bin/python3

import math
import os
import random
import re
import sys

"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors
and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they 
have.

Example m=6     cost=[1,3,4,5,6]
The two flavors that cost 1 and 5 meet the criteria. Output based on 1-based indexing
"""

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def get_indices(arr:list,value_i,value_j)->list:
    out=[]
    out.append(arr.index(value_i))
    try:
        out.append(arr.index(value_j,out[0]+1))
    except:
        out.append(arr.index(value_j,0,out[0]))
    for i in range(0,len(out)):
        out[i]+=1
    out.sort()
    return out

def icecreamParlor(m, arr):
    # Write your code here
    array=sorted(arr)
    i=0
    j=len(arr)-1
    #if left + right < value increment left
    #if left + right > value decrement right
    while(i<j):
        if(array[i]+array[j]<m):
            i+=1
        elif(array[i]+array[j]>m):
            j-=1
        else:
            return get_indices(arr,array[i],array[j])
    raise Exception
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
