#!/bin/python3

import math
import os
import random
import re
import sys

"""
* Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
* Declare an integer, lastAnswer, and initialize it to 0.
* There are 2 types of queries, given as an array of strings for you to parse:
        1. Query: 1 x y
            Let idx=((x (+) lastAnswer)%n).
            Append the integer y to arr[idx].
        2. Query: 2 x y
            Let idx=((x (+) lastAnswer)%n).
            Assign the value arr[idx][y%size(arr[idx])] to lastAnswer.
            Store the new value of lastAnswer to an answers array.
Note: (+) is the bitwise XOR operation, which corresponds to the ^ operator in most languages. 
% is the modulo operator. Finally, size(arr[idx]) is the number of elements in arr[idx]
"""

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr=[[] for _ in range(n)]
    last_answer=0
    answers=[]
    for q,x,y in queries:
        idx=(x^last_answer)%n
        if(q%2):
            arr[idx].append(y)
        else:
            last_answer=arr[idx][y%len(arr[idx])]
            answers.append(last_answer)
    return(answers)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
