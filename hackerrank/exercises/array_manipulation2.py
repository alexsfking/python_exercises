#!/bin/python3

import math
import os
import random
import re
import sys

'''
Starting with a 1-indexed array of zeros and a list of operations, for each
operation add a value to each the array element between two given indices,
inclusive. Once all operations have been performed, return the maximum value in
the array.

Example
n=10    queries=[[1,5,3],[4,8,7],[6,9,1]]
a   b   k
1   5   3
4   8   7
6   9   1

Add the values of k between the indices a and b inclusive:
index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]

The largest value is 10 after all operations are performed.
Return 10
'''

'''
This solution uses an array to keep track of the cumulative sum of all elements
from the start of the array up to each position. However, it initializes the
array with n+2 elements instead of n+1. This is because the solution uses the
value q[1]+1 in the loop, which may exceed the range of the array if the last
query covers the last element of the array. By adding an extra element to the
array, this solution can handle such cases without throwing an index out of
range error.

The solution then iterates over all queries, adding the query value k to the
start position of the range a and subtracting the same value k from the next
position after the end position of the range b+1. It then iterates over the
prefix sum array, computing the cumulative sum and keeping track of the maximum
value. The final result is the maximum value found after iterating over the
prefix sum array.

Overall, this solution is correct and should provide the correct output for the
arrayManipulation problem. It has a time complexity of O(M+N) and space
complexity of O(N), making it much faster than the naive solution.
'''

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr=[0]*(n+2)
    for q in queries:
        arr[q[0]]+=q[2]
        arr[q[1]+1]-=q[2]
    running_sum=0
    maximum=0
    for a in arr:
        running_sum+=a
        if running_sum>maximum:
            maximum=running_sum
    return maximum


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    #fptr.write(str(result) + '\n')

    #fptr.close()
