#!/bin/python3

import math
import os
import random
import re
import sys

'''
Hackerland is a one-dimensional city with houses aligned at integral locations along a road.
The Mayor wants to install radio transmitters on the roofs of the city's houses. Each
transmitter has a fixed range meaning it can transmit a signal to all houses within that
number of units distance away.

Given a map of Hackerland and the transmission range, determine the minimum number of
transmitters so that every house is within range of at least one transmitter. Each
transmitter must be installed on top of an existing house.

Example 1:
8 2
7 2 4 6 5 9 12 11
Sorted: 2 4 5 6 7 9 11 12
We can cover the entire city by installing 3 transmitters on houses at locations 4, 9, and 12.

Example 2:
7 2
9 5 4 2 6 15 12
Sorted: 2 4 5 6 9 12 15
We can cover the city by installing 4 transmitters on houses at locations 4, 9, 12, 15.
'''
#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#
      

def hackerlandRadioTransmitters(x, k):
    houses=(sorted(list(set(x))))
    i, transmitters = 0, 0
    while i < len(houses):
        j = i + 1
        while((j < len(houses)) and (houses[j] - houses[i] <= k)):
            j += 1
        transmitters += 1
        i = j
        while((i < len(houses)) and (houses[i] - houses[j-1] <= k)):
            i += 1
    return transmitters


'''
***Chat-GPT***
The function hackerlandRadioTransmitters takes two parameters:

    x which is a list of integers representing the positions of the houses in
    the city. k which is an integer representing the range of the transmitters.

The first thing the function does is to create a sorted list of unique house
positions using the sorted and set functions. This ensures that we are dealing
with a sorted list of unique house positions in ascending order.

The function then initializes two variables i and transmitters to 0. The
variable i will be used to iterate through the houses and transmitters will keep
track of the number of transmitters that are needed.

The function then enters a while loop that will iterate through the houses. The
inner while loop checks if the distance between the current house and the next
house is less than or equal to the range of the transmitter. If it is, then the
inner loop continues to check the next house until the distance between the
current house and the next house is greater than the range of the transmitter.
Once this is true, it means that we have found the farthest house that can be
covered by the transmitter from the current house. The function then increments
the transmitters variable and sets i to the next house position.

The function then enters another while loop that checks if there are any houses
that can still be covered by the current transmitter. If there are, it continues
to check the next house until the distance between the current house and the
last house covered by the transmitter is greater than the range of the
transmitter. Once this is true, it means that we have found the farthest house
that can be covered by the transmitter from the last house covered. The function
then sets i to the next house position.

Finally, the function returns the transmitters variable which represents the
minimum number of transmitters needed to cover all the houses in the city.

Overall, the function is implementing a greedy algorithm that iterates through
the sorted list of unique house positions and installs a transmitter on the
farthest house that can be covered by the transmitter from the current house.
This algorithm ensures that we install the minimum number of transmitters
required to cover all the houses in the city.
'''        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    #fptr.write(str(result) + '\n')

    #fptr.close()
