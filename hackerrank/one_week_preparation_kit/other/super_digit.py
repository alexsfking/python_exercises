#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
# We define super digit of an integer  using the following rules:
# Given an integer, we need to find the super digit of the integer.
# If x has only one digit, then its super digit is x .
# Otherwise, the super digit of x is equal to the super digit of 
# the sum of the digits of x.
# For example, the super digit of 9875=29=11=2
#

def superDigit(n, k):
    # Write your code here
    result=calculate(n)
    while(result>9):
        result=calculate(result)
    result*=k
    while(result>9):
        result=calculate(result)
    return result
        
def calculate(n):
    temp=list(str(n))
    return(sum(map(int,temp)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
