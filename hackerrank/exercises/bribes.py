#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. 
# Each person wears a sticker indicating their initial position in the queue from 1 
# to n. Any person can bribe the person directly in front of them to swap positions, 
# but they still wear their original sticker. One person can bribe at most two others.
# Determine the minimum number of bribes that took place to get to a given queue 
# order. Print the number of bribes, or, if anyone has bribed more than two people, 
# print Too chaotic.
#

def minimumBribes(q):
    # Write your code here
    out=""
    i=0
    end=len(q)-2
    swaps=0
    if(len(q)>2):
        for j in range(len(q)):
            if(q[j]-(j+1)>2):
                out="Too chaotic"
                break
        if(not(out)):
            while(not is_sorted_index_and_values(q)):
                while(i<end):
                    temp_swaps,temp_list=calculate_swaps(q[i:i+3])
                    swaps+=temp_swaps
                    for index,value in enumerate(temp_list):
                        q[i+index]=temp_list[index]
                    i+=1
                i=0
            
    if(out):
        print(out)
    else:
        print(swaps)

def calculate_swaps(subset:list)->tuple:
    count=0
    while not(is_sorted(subset)):
        for i in range(0,len(subset)-1):
            if(subset[i]>subset[i+1]):
                temp=subset[i]
                subset[i]=subset[i+1]
                subset[i+1]=temp
                count+=1
    return(count,subset)

def is_sorted_index_and_values(l:list)->bool:
    for index,value in enumerate(l):
        if((index+1)!=value):
            return False
    return True

def is_sorted(l:list)->bool:
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            return False
    return True
        
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
