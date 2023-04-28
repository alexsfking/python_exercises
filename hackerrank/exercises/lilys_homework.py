#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def min_swaps(arr, vec)->int:
    swaps=0
    i=0
    while i<len(arr):
        if vec[i]['val']!=arr[i]:
            vec[vec[i]['idx']],vec[i]=vec[i],vec[vec[i]['idx']]
            swaps+=1
        else:
            i+=1
    return swaps

def lilysHomework(arr):
    # Write your code here
    vec = [{"val": arr[i], "idx": i} for i in range(len(arr))]
    return min(min_swaps(arr, sorted(vec,key=lambda x:x['val'])),min_swaps(arr, sorted(vec,key=lambda x:x['val'], reverse=True)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
