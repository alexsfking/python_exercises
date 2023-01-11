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

#another testers function
def minimumBribesX(q):
    q = [e-1 for e in q] # adjust to 0-index for simplicity
    bribes = 0
    for i in range(len(q)-1):
        if q[i] - i > 2:
            print("Too chaotic")
            return
        j = i
        while j >= 0 and q[j+1] < q[j]:
            q[j+1], q[j] = q[j], q[j+1]
            bribes += 1
            j -= 1
            print(q)
    print(bribes)

#chat-gpts response to the question
def minimumBribes(q):
    n = len(q)
    bribes = 0
    for i in range(n - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
            print(i,j,q[j],">",q[i],q[j]>q[i],bribes)
    print(bribes)

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
