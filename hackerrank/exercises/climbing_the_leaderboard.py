#!/bin/python3

import math
import os
import random
import re
import sys

"""
An arcade game player wants to climb to the top of the leaderboard and track their ranking.
The game uses Dense Ranking, so its leaderboard works like this:

    #   The player with the highest score is ranked number 1 on the leaderboard.
    #   Players who have equal scores receive the same ranking number, and the next 
        player(s) receive the immediately following ranking number.

"""

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked=sorted(list(set(ranked)),reverse=True)   
    out=[]
    for score in player:
        while(ranked and ranked[-1]<=score):
            ranked.pop()
        out.append(len(ranked)+1)
        
    return out
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
