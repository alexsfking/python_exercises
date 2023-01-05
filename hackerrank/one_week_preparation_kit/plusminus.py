#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_pos=0
    count_neg=0
    count_zero=0
    
    for e in arr:
        if(e>0):
            count_pos=count_pos+1
        elif(e<0):
            count_neg=count_neg+1
        else:
            count_zero=count_zero+1
    
    total=count_pos+count_neg+count_zero
    if(total):
        print("{0:.6f}".format(count_pos/total))
        print("{0:.6f}".format(count_neg/total))
        print("{0:.6f}".format(count_zero/total))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
