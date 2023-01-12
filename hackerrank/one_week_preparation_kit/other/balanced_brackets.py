#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# Given n strings of brackets, determine whether each sequence of brackets
# is balanced. If a string is balanced, return YES. Otherwise, return NO.
#

def isBalanced(s):
    # Write your code here
    stack=[]
    open_brackets=set(["[","{","("])
    closed_brackets=set(["]","}",")"])
    for c in s:
        if(c in open_brackets):
            stack.append(c)
        elif(c in closed_brackets):
            if(not stack):
                return "NO"
            if(stack[-1]=="[" and c=="]"):
                stack.pop()
            elif(stack[-1]=="{" and c=="}"):
                stack.pop()
            elif(stack[-1]=="(" and c==")"):
                stack.pop()
            else:
                return "NO"
        else:
            raise Exception()
    if(stack):
        return "NO"
    return "YES"
                
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
