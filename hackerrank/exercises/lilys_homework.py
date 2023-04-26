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

def min_swaps(arr)->int:
    swaps=0
    return swaps

def lilysHomework(arr):
    # Write your code here
    sorted_arr_ascending=sorted(arr)
    sorted_arr_descending=sorted(arr,reverse=True)
    vec = [{"val": arr[i], "idx": i} for i in range(len(arr))]
    return min(min_swaps(arr,sorted_arr_ascending, vec),min_swaps(arr,sorted_arr_descending, vec))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
