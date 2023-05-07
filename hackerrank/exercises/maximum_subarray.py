#!/bin/python3

import math
import os
import random
import re
import sys

"""
We define subsequence as any subset of an array. We define a subarray as a
contiguous subsequence in an array.

Given an array, find the maximum possible sum among:

    1. all nonempty subarrays.
    2. all nonempty subsequences.
    Print the two values as space-separated integers on one line.

Note that empty subarrays/subsequences should not be considered.

Example
Input
2 
4 
1 2 3 4
6
2 -1 2 3 4 -5

Output
10 10
10 11

In the first case:
The max sum for both contiguous and non-contiguous elements is the sum of ALL
the elements (as they are all positive).

In the second case:
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum. For
the max sum of a not-necessarily-contiguous group of elements, simply add all
the positive elements.
"""

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    max_max=max_current=arr[0]
    #in the event arr[0] is negative and the array is all negative
    max_subsequence = max(arr[0], 0)

    for i in range(1,len(arr)):
        #start a new sub array or continue the previous subarray
        max_current=max(arr[i],max_current+arr[i])
        #keep track of the maximum subarray
        max_max=max(max_max,max_current)
        #calculate the maximum subsequence
        if(arr[i]>0):
            max_subsequence+=arr[i]
    
    if(max_subsequence==0):
        #in the event all values are negative
        max_subsequence=max_max
    return(max_max,max_subsequence)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
