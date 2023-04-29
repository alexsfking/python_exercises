#!/bin/python3

import math
import os
import random
import re
import sys

'''
calculate the minimum number of swaps to make an array "beautiful"

that is the minimum sum of the absolute value of consecutive elements

for example 

0 1 2 3 4 5 requires 0 swaps
5 4 3 2 1 0 requires 0 swaps
5 1 2 3 4 0 requires 1 swap
0 4 3 2 5 1 requires 2 swaps
'''

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def min_swaps(arr:list[int], vec:list[dict[str,int]])->int:
    swaps=0
    i=0
    while i<len(arr):
        if vec[i]['val']!=arr[i]:
            vec[vec[i]['idx']],vec[i]=vec[i],vec[vec[i]['idx']]
            swaps+=1
        else:
            i+=1
    return swaps

def lilysHomework(arr:list[int])->int:
    # Write your code here
    vec = [{"val": arr[i], "idx": i} for i in range(len(arr))]
    ascending_vec=sorted(vec,key=lambda x:x['val'])
    descending_vec=sorted(vec,key=lambda x:x['val'], reverse=True)
    return min(min_swaps(arr, ascending_vec),min_swaps(arr, descending_vec))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
