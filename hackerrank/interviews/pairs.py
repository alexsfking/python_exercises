"""
Given an array of integers and a target value, determine the number of pairs of array elements that have a
difference equal to the target value.

Example
k=1
arr=[1,2,3,4]
pairs:
    for k=1    2-1=1   3-2=1   4-3=1
    3 pairs. Return 3
"""

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER k
# 2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here
    values=set(arr)
    count=0
    for a in arr:
        if(a>k):
            if (a-k) in values:
                count+=1
    return count