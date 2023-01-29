#!/bin/python3

import math
import os
import random
import re
import sys

# Given an integer n, find each x such that:
#     0<=x<=n
#     n+x=n(bitwise XOR)x

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    if(n==0):
        return 1
    count=0
    n=bin(n)[2:]
    for c in list(n):
        if(c=='0'):
            count+=1
    return(pow(2,count))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
