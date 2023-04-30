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

'''
This Python code defines a function called lilysHomework that calculates the
minimum number of swaps needed to make an array "beautiful". A beautiful array
is defined as an array where the sum of the absolute value of consecutive
elements is minimum.

The code uses two helper functions: min_swaps and __main__.

The min_swaps function takes in two arguments: an integer list arr and a list of
dictionaries vec. It returns the minimum number of swaps needed to make the arr
argument beautiful using the vec list of dictionaries to track the original
index of each element in the arr. The function swaps adjacent elements in the
arr to minimize the sum of the absolute value of consecutive elements.

The lilysHomework function takes in an integer list arr as an argument. It
creates two lists of dictionaries called ascending_vec and descending_vec that
track the original index of each element in the arr and sorts them in ascending
and descending order, respectively. The function then returns the minimum of the
number of swaps needed to make arr beautiful using ascending_vec and
descending_vec using the min_swaps function.

The code also has a __main__ block that reads in input values, calls the
lilysHomework function, and writes the output to a file. However, the input and
output file paths are not specified, and the code is intended to be run in a
specific environment with the os.environ['OUTPUT_PATH'] variable defined.
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
