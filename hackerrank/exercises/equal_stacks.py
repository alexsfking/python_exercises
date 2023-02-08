#!/bin/python3

import math
import os
import random
import re
import sys

"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height.
You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height.
This means you must remove zero or more cylinders from the top of zero or more of the three stacks until
they are all the same height, then return the height.

STDIN       Function
-----       --------
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]

reverse h1,h2,h3

h1 = [1, 1, 1, 2, 3]
h2 = [2, 3, 4]
h3 = [1, 4, 1, 1]

h1_cumulative=[1,2,3,5,8]
h2_cumulative=[2,5,9]
h3_cumulative=[1,5,6,7]

discard until equal
h1_cumulative=[1,2,3,5]
h2_cumulative=[2,5]
h3_cumulative=[1,5]

return 5
"""

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

class Stacks():
    def __init__(self, *args):
        self.stack_list=[]
        for a in args:
            self.stack_list.append(Stack(a))
        
    def get_heights(self)->list:
        return [x.get_height() for x in self.stack_list]
    
    def get_smallest(self,heights:list)->int:
        return min(heights)
    
    def discard_until(self, until:int):
        for s in self.stack_list:
            while(s.get_height()>until):
                s.discard()
    
    def get_cumulative_lists(self):
        return [x.get_cumulative_list() for x in self.stack_list]
    
    def success(self, heights:list):
        if(all(x == heights[0] for x in heights)):
            return True            
    
    def calculate(self)->int:
        heights=self.get_heights()
        while(not self.success(heights)):
            self.discard_until(self.get_smallest(heights))
            heights=self.get_heights()
        return heights[0]
        

class Stack():
    def __init__(self,s_list):
        self.cumulative=[]
        self.cumulative.append(s_list.pop())
        while(s_list):
            self.cumulative.append(s_list.pop()+self.cumulative[-1])
            
    def get_height(self)->int:
        try:
            return self.cumulative[-1]
        except IndexError:
            return 0
    
    def discard(self):
        self.cumulative.pop()
            
    def get_stack_length(self)->int:
        return len(self.cumulative)
    
    def get_cumulative_list(self)->list:
        return self.cumulative

def equalStacks(h1, h2, h3):
    # Write your code here
    stacks=Stacks(h1,h2,h3)
    return stacks.calculate()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
