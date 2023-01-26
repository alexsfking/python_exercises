#!/bin/python3

import math
import os
import random
import re
import sys

"""
You will be given a list of integers, arr, and a single integer k. You must create an array
of length k from elements of arr such that its unfairness is minimized. Call that array arr'.
Unfairness of an array is calculated as

        max(arr')-min(arr')
        where max denotes the largest integer in arr' and min the smallest respectivetly

Example
    arr=[1,4,7,2]       k=2
    arr'=[4,7]      unfairness=max(4,7)-min(4,7)
                              =3
    Testing all pairs gives arr'=[1,2]
                    unfairness=1
* integers in arr need to be unique
"""

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    diff=[]
    arr=sorted(arr,reverse=True)
    length=len(arr)+1-k
    for start in range(0,length):
        diff.append(arr[start]-arr[start+k-1])
        start+=1   
    return(min(diff))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
